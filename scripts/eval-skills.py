#!/usr/bin/env python3
"""
eval-skills.py — Score all skills based on usage telemetry.

Reads:  .telemetry/sessions/*.json
Writes: skills/{category}/{name}/SKILL.md (updates stats section)
        intelligence/skills-performance.md

Usage:
    python3 scripts/eval-skills.py              # update all skills
    python3 scripts/eval-skills.py --report     # show skills report
    python3 scripts/eval-skills.py skills/saas/migration/SKILL.md  # one skill
"""
import sys, json, re, datetime
from pathlib import Path
from collections import defaultdict

TELEMETRY = Path(".telemetry/sessions")
INTEL = Path("intelligence/skills-performance.md")


def load_sessions():
    if not TELEMETRY.exists():
        return []
    return [json.loads(f.read_text()) for f in TELEMETRY.glob("*.json")]


def compute_skill_stats(sessions):
    stats = defaultdict(lambda: {"used": 0, "shipped": 0, "pdca_total": 0, "failures": []})
    for s in sessions:
        for skill in s.get("skills_used", []):
            sk = stats[skill]
            sk["used"] += 1
            if s.get("feature_shipped"): sk["shipped"] += 1
            sk["pdca_total"] += s.get("pdca_iterations", 0)
            for e in s.get("errors", []):
                if not e.get("resolved"):
                    sk["failures"].append(e.get("type", "unknown"))
    return stats


def update_skill_metadata(skill_path, skill_stats):
    path = Path(skill_path)
    if not path.exists():
        return False

    content = path.read_text()
    if "Skill Metadata" not in content:
        return False

    used = skill_stats.get("used", 0)
    shipped = skill_stats.get("shipped", 0)
    pdca_total = skill_stats.get("pdca_total", 0)
    ship_rate = f"{(shipped/used*100):.0f}%" if used > 0 else "0%"
    avg_pdca = f"{pdca_total/used:.1f}" if used > 0 else "0.0"
    today = datetime.date.today().isoformat()

    failures = list(set(skill_stats.get("failures", [])))[:3]
    failures_yaml = "\n".join(f"    - {f}" for f in failures) if failures else "    []"

    # Update stats block in the YAML
    def replace_stat(content, key, value):
        return re.sub(
            rf"(  {key}:).*",
            f"\g<1> {value}",
            content
        )

    content = replace_stat(content, "times_used", used)
    content = replace_stat(content, "avg_pdca_iterations_when_used", avg_pdca)
    content = replace_stat(content, "ship_rate_when_used", f'"{ship_rate}"')
    if used > 0:
        content = replace_stat(content, "last_used", f'"{today}"')

    # Replace failure_patterns
    content = re.sub(
        r"failure_patterns:.*?(?=improvement_log:|$)",
        f"failure_patterns:\n{failures_yaml}\n\n",
        content,
        flags=re.DOTALL
    )

    path.write_text(content)
    return True


def generate_report(skill_stats):
    today = datetime.date.today().isoformat()
    lines = [
        "# Skills Performance Report",
        f"> Generated: {today}",
        "",
        "## Rankings (by ship rate)",
        "",
        "| Skill | Used | Ship Rate | Avg PDCA | Status |",
        "|-------|------|-----------|----------|--------|",
    ]

    ranked = []
    for skill, stats in skill_stats.items():
        used = stats["used"]
        if used == 0:
            ranked.append((skill, 0, 0, "unused"))
            continue
        ship_rate = stats["shipped"] / used * 100
        avg_pdca = stats["pdca_total"] / used
        status = "excellent" if ship_rate >= 90 and avg_pdca <= 1.5 else                  "good" if ship_rate >= 70 else                  "needs-improvement"
        ranked.append((skill, ship_rate, avg_pdca, status))

    ranked.sort(key=lambda x: (-x[1], x[2]))

    for skill, ship_rate, avg_pdca, status in ranked:
        icon = "✓" if "good" in status or "excellent" in status else                "-" if status == "unused" else "⚠"
        lines.append(
            f"| {skill:<40} | "
            f"{skill_stats[skill]['used']:>4} | "
            f"{ship_rate:>5.0f}% | "
            f"{avg_pdca:>6.1f} | "
            f"{icon} {status} |"
        )

    # Improvement candidates
    needs_work = [
        (s, r, p) for s, r, p, st in ranked
        if st == "needs-improvement" or p > 2.5
    ]

    if needs_work:
        lines += ["", "## Skills Needing Improvement", ""]
        for skill, rate, pdca in needs_work[:5]:
            lines.append(f"- **{skill}**: {rate:.0f}% ship rate, {pdca:.1f} avg PDCA")
            lines.append(f"  Run: `/improve-skill {skill}` to generate improvements")

    unused = [s for s, r, p, st in ranked if st == "unused"]
    if unused:
        lines += ["", "## Unused Skills (consider removing or promoting)", ""]
        for s in unused[:5]:
            lines.append(f"- {s}")

    return "\n".join(lines)


def main():
    sessions = load_sessions()
    skill_stats = compute_skill_stats(sessions)

    if "--report" in sys.argv:
        print(generate_report(skill_stats))
        return

    target = None
    for arg in sys.argv[1:]:
        if arg.startswith("skills/"):
            target = arg
            break

    if target:
        skill_name = Path(target).parent.name
        stats = skill_stats.get(skill_name, {"used": 0, "shipped": 0, "pdca_total": 0, "failures": []})
        if update_skill_metadata(target, stats):
            print(f"Updated: {target}")
        else:
            print(f"Could not update: {target}")
        return

    # Update all skills
    updated = 0
    for skill_file in sorted(Path("skills").rglob("SKILL.md")):
        skill_name = skill_file.parent.name
        stats = skill_stats.get(skill_name, {"used": 0, "shipped": 0, "pdca_total": 0, "failures": []})
        if update_skill_metadata(str(skill_file), stats):
            updated += 1

    print(f"Updated {updated} skills")

    # Write performance report
    report = generate_report(skill_stats)
    INTEL.parent.mkdir(exist_ok=True)
    INTEL.write_text(report)
    print(f"Written: {INTEL}")


if __name__ == "__main__":
    main()
