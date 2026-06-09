#!/usr/bin/env python3
"""
eval-agents.py — Score all agents based on usage telemetry.

Reads:  .telemetry/sessions/*.json
Writes: agents/*.md (updates performance stats)
        intelligence/agents-performance.md
"""
import sys, json, re, datetime
from pathlib import Path
from collections import defaultdict

TELEMETRY = Path(".telemetry/sessions")
INTEL = Path("intelligence/agents-performance.md")


def load_sessions():
    if not TELEMETRY.exists(): return []
    return [json.loads(f.read_text()) for f in TELEMETRY.glob("*.json")]


def compute_agent_stats(sessions):
    stats = defaultdict(lambda: {"activated": 0, "shipped": 0, "pdca_total": 0, "failures": []})
    for s in sessions:
        for agent in s.get("agents_used", []):
            ag = stats[agent]
            ag["activated"] += 1
            if s.get("feature_shipped"): ag["shipped"] += 1
            ag["pdca_total"] += s.get("pdca_iterations", 0)
            for e in s.get("errors", []):
                if not e.get("resolved"):
                    ag["failures"].append(e.get("type", "unknown"))
    return stats


def update_agent_metadata(agent_path, agent_stats):
    path = Path(agent_path)
    if not path.exists(): return False
    content = path.read_text()
    if "Agent Performance" not in content: return False

    activated = agent_stats.get("activated", 0)
    shipped = agent_stats.get("shipped", 0)
    pdca_total = agent_stats.get("pdca_total", 0)
    ship_rate = f"{(shipped/activated*100):.0f}%" if activated > 0 else "0%"
    avg_pdca = f"{pdca_total/activated:.1f}" if activated > 0 else "0.0"
    today = datetime.date.today().isoformat()

    def rep(c, key, val):
        return re.sub(rf"(  {key}:).*", f"\\g<1> {val}", c)

    content = rep(content, "sessions_activated", activated)
    content = rep(content, "features_shipped", shipped)
    content = rep(content, "avg_pdca_iterations", avg_pdca)
    content = rep(content, "ship_rate", f'"{ship_rate}"')
    if activated > 0:
        content = rep(content, "last_activated", f'"{today}"')

    path.write_text(content)
    return True


def generate_report(agent_stats):
    today = datetime.date.today().isoformat()
    lines = [
        "# Agents Performance Report",
        f"> Generated: {today}",
        "",
        "## Agent Rankings",
        "",
        "| Agent | Activations | Ship Rate | Avg PDCA | Status |",
        "|-------|-------------|-----------|----------|--------|",
    ]

    ranked = []
    for agent, stats in agent_stats.items():
        activated = stats["activated"]
        if activated == 0:
            ranked.append((agent, 0, 0, "unused"))
            continue
        sr = stats["shipped"] / activated * 100
        ap = stats["pdca_total"] / activated
        status = "excellent" if sr >= 90 and ap <= 1.5 else "good" if sr >= 70 else "needs-improvement"
        ranked.append((agent, sr, ap, status))

    ranked.sort(key=lambda x: (-x[1], x[2]))
    for agent, sr, ap, status in ranked:
        icon = "✓" if "good" in status or "excellent" in status else "-" if status == "unused" else "⚠"
        lines.append(
            f"| {agent:<40} | {agent_stats[agent]['activated']:>11} | "
            f"{sr:>5.0f}% | {ap:>6.1f} | {icon} {status} |"
        )

    return "\n".join(lines)


def main():
    sessions = load_sessions()
    agent_stats = compute_agent_stats(sessions)
    updated = 0
    for agent_file in sorted(Path("agents").glob("*.md")):
        agent_name = agent_file.stem
        stats = agent_stats.get(agent_name, {"activated": 0, "shipped": 0, "pdca_total": 0, "failures": []})
        if update_agent_metadata(str(agent_file), stats): updated += 1

    print(f"Updated {updated} agents")
    report = generate_report(agent_stats)
    INTEL.parent.mkdir(exist_ok=True)
    INTEL.write_text(report)
    print(f"Written: {INTEL}")


if __name__ == "__main__":
    main()
