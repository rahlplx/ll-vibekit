#!/usr/bin/env python3
"""
improve-skill.py — Analyze a skill's failure patterns and suggest improvements.

Reads:  skills/{cat}/{name}/SKILL.md (stats + failure_patterns)
        .telemetry/sessions/*.json (recent failures when this skill was used)
Prints: Improvement suggestions for the human or agent to apply

Usage:
    python3 scripts/improve-skill.py skills/saas/migration/SKILL.md
    python3 scripts/improve-skill.py --all-underperforming
"""
import sys, json, re
from pathlib import Path
from collections import Counter

TELEMETRY = Path(".telemetry/sessions")


def load_skill(path):
    content = Path(path).read_text()
    stats = {}
    if "times_used:" in content:
        m = re.search(r"times_used:\s*(\d+)", content)
        if m: stats["times_used"] = int(m.group(1))
        m = re.search(r"avg_pdca_iterations_when_used:\s*([\d.]+)", content)
        if m: stats["avg_pdca"] = float(m.group(1))
        m = re.search(r'ship_rate_when_used:\s*"?(\d+)%"?', content)
        if m: stats["ship_rate"] = int(m.group(1))
    return content, stats


def find_sessions_using_skill(skill_name):
    if not TELEMETRY.exists(): return []
    sessions = [json.loads(f.read_text()) for f in TELEMETRY.glob("*.json")]
    return [s for s in sessions if skill_name in s.get("skills_used", [])]


def generate_suggestions(skill_path, content, stats, sessions):
    skill_name = Path(skill_path).parent.name
    suggestions = []

    used = stats.get("times_used", 0)
    ship_rate = stats.get("ship_rate", 0)
    avg_pdca = stats.get("avg_pdca", 0)

    if used == 0:
        suggestions.append({
            "type": "unused",
            "priority": "low",
            "suggestion": "Skill has never been used. Consider: (1) promote it in SKILLS-REGISTRY.md, (2) add it to relevant agent files, (3) remove if redundant."
        })
        return suggestions

    if ship_rate < 70:
        error_types = Counter()
        for s in sessions:
            if not s.get("feature_shipped"):
                for e in s.get("errors", []):
                    error_types[e.get("type", "unknown")] += 1

        top_error = error_types.most_common(1)
        if top_error:
            suggestions.append({
                "type": "high_failure_rate",
                "priority": "high",
                "suggestion": f"Ship rate {ship_rate}% is below 70%. Most common error when this skill is used: '{top_error[0][0]}' ({top_error[0][1]} times). Add a warning about this to the skill's Rules section."
            })
        else:
            suggestions.append({
                "type": "high_failure_rate",
                "priority": "high",
                "suggestion": f"Ship rate {ship_rate}% is below 70%. Review recent sessions where this skill was used but feature did not ship."
            })

    if avg_pdca > 2.5:
        suggestions.append({
            "type": "high_iterations",
            "priority": "medium",
            "suggestion": f"Average {avg_pdca:.1f} PDCA iterations when this skill is used. The Steps section may be missing a critical step that causes rework. Review the most recent 3 sessions."
        })

    if "## Eval Criteria" not in content:
        suggestions.append({
            "type": "missing_eval",
            "priority": "medium",
            "suggestion": "Add an '## Eval Criteria' section defining what success looks like when this skill is applied."
        })

    if used < 3 and used > 0:
        suggestions.append({
            "type": "low_usage",
            "priority": "low",
            "suggestion": f"Only used {used} times. Not enough data for reliable scoring. Use more before optimizing."
        })

    if not suggestions:
        suggestions.append({
            "type": "performing_well",
            "priority": "none",
            "suggestion": f"Skill performing well: {ship_rate}% ship rate, {avg_pdca:.1f} avg PDCA. No improvements needed."
        })

    return suggestions


def find_underperforming():
    results = []
    for skill_file in sorted(Path("skills").rglob("SKILL.md")):
        _, stats = load_skill(str(skill_file))
        used = stats.get("times_used", 0)
        ship_rate = stats.get("ship_rate", 100)
        avg_pdca = stats.get("avg_pdca", 0)
        if used > 0 and (ship_rate < 70 or avg_pdca > 2.5):
            results.append((str(skill_file), ship_rate, avg_pdca, used))
    results.sort(key=lambda x: x[1])
    return results


def main():
    if "--all-underperforming" in sys.argv:
        underperforming = find_underperforming()
        if not underperforming:
            print("No underperforming skills found (or no data yet).")
            return
        print(f"Underperforming skills ({len(underperforming)}):")
        for path, sr, ap, used in underperforming:
            print(f"  {path}: {sr}% ship, {ap:.1f} PDCA, {used} uses")
            print(f"  Run: python3 scripts/improve-skill.py {path}")
        return

    if len(sys.argv) < 2 or not sys.argv[1].startswith("skills/"):
        print("Usage: python3 scripts/improve-skill.py skills/category/name/SKILL.md")
        print("       python3 scripts/improve-skill.py --all-underperforming")
        return

    skill_path = sys.argv[1]
    content, stats = load_skill(skill_path)
    skill_name = Path(skill_path).parent.name
    sessions = find_sessions_using_skill(skill_name)
    suggestions = generate_suggestions(skill_path, content, stats, sessions)

    print(f"Improvement Analysis: {skill_path}")
    print(f"Stats: {stats.get('times_used',0)} uses | {stats.get('ship_rate',0)}% ship | {stats.get('avg_pdca',0):.1f} avg PDCA")
    print()
    for s in suggestions:
        icon = "!!" if s["priority"] == "high" else ">" if s["priority"] == "medium" else "-"
        print(f"[{s['priority'].upper()}] {icon} {s['type']}")
        print(f"   {s['suggestion']}")
        print()


if __name__ == "__main__":
    main()
