#!/usr/bin/env python3
"""
harness-health.py — Full harness health check.

Checks: skills, agents, memory files, commands, telemetry
Scores each area 0-100
Generates: intelligence/harness-health-{date}.md

Usage:
    python3 scripts/harness-health.py
    python3 scripts/harness-health.py --fix  # attempt auto-fixes
"""
import sys, json, re, datetime
from pathlib import Path

TODAY = datetime.date.today().isoformat()
TELEMETRY = Path(".telemetry/sessions")


def check_skills():
    issues = []
    skills = list(Path("skills").rglob("SKILL.md"))
    for s in skills:
        content = s.read_text()
        if "## When to Use" not in content and "## WHEN TO USE" not in content:
            issues.append(f"Missing 'When to Use': {s}")
        if "## Skill Metadata" not in content:
            issues.append(f"Missing metadata: {s}")
        if len(content) < 300:
            issues.append(f"Too short (<300 chars): {s}")
    score = max(0, 100 - len(issues) * 5)
    return score, issues, len(skills)


def check_agents():
    issues = []
    agents = list(Path("agents").glob("*.md"))
    for a in agents:
        content = a.read_text()
        if "## Role" not in content and "## ROLE" not in content:
            issues.append(f"Missing Role section: {a}")
        if "## Agent Performance" not in content:
            issues.append(f"Missing Performance tracking: {a}")
        if "## Self-Eval Checklist" not in content:
            issues.append(f"Missing Self-Eval: {a}")
    score = max(0, 100 - len(issues) * 8)
    return score, issues, len(agents)


def check_memory():
    issues = []
    required = ["MEMORY/stack.md", "MEMORY/patterns.md",
                "MEMORY/mistakes.md", "MEMORY/modules.md"]
    for f in required:
        if not Path(f).exists():
            issues.append(f"Missing: {f}")
            continue
        content = Path(f).read_text()
        if len(content) < 100:
            issues.append(f"Stub (< 100 chars): {f}")
        if "{fill}" in content.lower():
            issues.append(f"Unfilled template: {f}")
    score = max(0, 100 - len(issues) * 20)
    return score, issues


def check_project_config():
    issues = []
    if not Path("PROJECT.md").exists():
        issues.append("PROJECT.md missing — run /setup to generate it")
    elif "{fill}" in Path("PROJECT.md").read_text():
        issues.append("PROJECT.md has unfilled sections — run /setup discover")

    if not Path(".vibekit.json").exists():
        issues.append(".vibekit.json missing — copy from ll-vibekit/.vibekit.json and fill in")
    else:
        try:
            cfg = json.loads(Path(".vibekit.json").read_text())
            if "your-project" in cfg.get("project_name",""):
                issues.append(".vibekit.json has default project_name — fill in your project name")
            cmds = cfg.get("test_commands",{})
            for k, v in cmds.items():
                if "Set your" in v:
                    issues.append(f".vibekit.json test_commands.{k} not configured")
        except: issues.append(".vibekit.json is invalid JSON")

    score = max(0, 100 - len(issues) * 25)
    return score, issues


def check_commands():
    required = ["generate-prp", "execute-prp", "route", "eval-prp",
                "eval", "report", "setup", "deploy", "status"]
    issues = []
    cmd_dir = Path(".claude/commands")
    for cmd in required:
        if not (cmd_dir / f"{cmd}.md").exists():
            issues.append(f"Missing command: /{cmd}")
    score = max(0, 100 - len(issues) * 10)
    return score, issues


def check_telemetry():
    issues = []
    if not TELEMETRY.exists() or not list(TELEMETRY.glob("*.json")):
        issues.append("No sessions recorded yet — this is normal for new installs")
        return 50, issues, 0  # neutral score for new installs

    sessions = [json.loads(f.read_text()) for f in TELEMETRY.glob("*.json")]
    total = len(sessions)
    shipped = sum(1 for s in sessions if s.get("feature_shipped"))
    ship_rate = shipped / total * 100 if total > 0 else 0

    if ship_rate < 50 and total >= 5:
        issues.append(f"Low ship rate: {ship_rate:.0f}% — review MEMORY/mistakes.md")
    avg_pdca = sum(s.get("pdca_iterations",0) for s in sessions) / total
    if avg_pdca > 3 and total >= 5:
        issues.append(f"High avg PDCA: {avg_pdca:.1f} — review PRPs quality with /eval-prp")

    score = min(100, 50 + int(ship_rate / 2))
    return score, issues, total


def print_section(name, score, issues, extra=""):
    icon = "✓" if score >= 80 else "~" if score >= 60 else "✗"
    print(f"  {icon} {name}: {score}/100  {extra}")
    for issue in issues[:3]:
        print(f"      - {issue}")
    if len(issues) > 3:
        print(f"      ... +{len(issues)-3} more")


def main():
    print(f"\n=== ll-vibekit Harness Health Check — {TODAY} ===\n")

    sk_score, sk_issues, sk_count = check_skills()
    ag_score, ag_issues, ag_count = check_agents()
    mem_score, mem_issues = check_memory()
    proj_score, proj_issues = check_project_config()
    cmd_score, cmd_issues = check_commands()
    tel_score, tel_issues, tel_count = check_telemetry()

    print_section("Skills", sk_score, sk_issues, f"({sk_count} skills)")
    print_section("Agents", ag_score, ag_issues, f"({ag_count} agents)")
    print_section("Memory", mem_score, mem_issues)
    print_section("Project Config", proj_score, proj_issues)
    print_section("Commands", cmd_score, cmd_issues)
    print_section("Telemetry", tel_score, tel_issues, f"({tel_count} sessions)")

    overall = int((sk_score + ag_score + mem_score + proj_score + cmd_score + tel_score) / 6)
    grade = "EXCELLENT" if overall >= 90 else "GOOD" if overall >= 75 else             "NEEDS WORK" if overall >= 60 else "CRITICAL"
    print(f"\nOVERALL: {overall}/100 — {grade}")

    if "--fix" in sys.argv:
        print("\nAuto-fix: running eval-skills + eval-agents + intelligence-report...")
        import subprocess
        subprocess.run(["python3", "scripts/eval-skills.py"])
        subprocess.run(["python3", "scripts/eval-agents.py"])
        subprocess.run(["python3", "scripts/intelligence-report.py", "--update"])


if __name__ == "__main__":
    main()
