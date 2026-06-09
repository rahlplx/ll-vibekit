#!/usr/bin/env python3
"""intelligence-report.py -- Weekly harness intelligence report.
Usage:
    python3 scripts/intelligence-report.py           # full report
    python3 scripts/intelligence-report.py --update  # update INTELLIGENCE.md stats
"""
import sys, json, datetime, re
from pathlib import Path
from collections import Counter

TELEMETRY = Path(".telemetry/sessions")
INTEL = Path("intelligence/INTELLIGENCE.md")

def load_all():
    if not TELEMETRY.exists(): return []
    return [json.loads(f.read_text()) for f in TELEMETRY.glob("*.json")]

def stats(sessions):
    if not sessions: return {}
    n = len(sessions)
    shipped = sum(1 for s in sessions if s.get("feature_shipped"))
    avg_p = sum(s.get("pdca_iterations",0) for s in sessions) / n
    agents = Counter(a for s in sessions for a in s.get("agents_used",[]))
    skills = Counter(sk for s in sessions for sk in s.get("skills_used",[]))
    errors = Counter(e.get("type","?") for s in sessions for e in s.get("errors",[]))
    return {"n": n, "shipped": shipped, "rate": f"{shipped/n*100:.0f}%",
            "avg_pdca": f"{avg_p:.1f}", "agents": agents.most_common(3),
            "skills": skills.most_common(3), "errors": errors.most_common(3)}

def suggestions(st):
    s = []
    if st.get("errors") and st["errors"][0][1] >= 3:
        s.append(f"Error '{st[chr(101)+chr(114)+chr(114)+chr(111)+chr(114)+chr(115)][0][0]}' occurred {st[chr(101)+chr(114)+chr(114)+chr(111)+chr(114)+chr(115)][0][1]}x -- add to MEMORY/mistakes.md")
    avg = float(st.get("avg_pdca","0"))
    if avg > 3: s.append(f"Avg {avg} PDCA iterations -- run /eval-prp on recent PRPs")
    rate = float(st.get("rate","0%").rstrip("%"))
    if rate < 70 and st.get("n",0) >= 5: s.append("Ship rate < 70% -- review HUMAN-TODO.md for blockers")
    return s or ["Harness performing well -- keep shipping!"]

def update_intel(st):
    if not INTEL.exists(): return
    today = datetime.date.today().isoformat()
    content = INTEL.read_text()
    new_line = f"Sessions logged: {st.get(chr(110),0)}  |  Ship rate: {st.get(chr(114)+chr(97)+chr(116)+chr(101),chr(48)+chr(37))}  |  Avg PDCA: {st.get(chr(97)+chr(118)+chr(103)+chr(95)+chr(112)+chr(100)+chr(99)+chr(97),chr(48))}  |  Updated: {today}"
    content = re.sub(r"Sessions logged:.*", new_line, content, count=1)
    INTEL.write_text(content)
    print(f"Updated intelligence/INTELLIGENCE.md")

def main():
    sessions = load_all()
    st = stats(sessions)
    if "--update" in sys.argv:
        if st: update_intel(st)
        else: print("No sessions yet.")
        return
    if not sessions: print("No sessions yet."); return
    today = datetime.date.today().isoformat()
    lines = [f"# Intelligence Report -- {today}", "",
             f"Sessions: {st[chr(110)]}  |  Shipped: {st[chr(115)+chr(104)+chr(105)+chr(112)+chr(112)+chr(101)+chr(100)]}  |  Rate: {st[chr(114)+chr(97)+chr(116)+chr(101)]}  |  Avg PDCA: {st[chr(97)+chr(118)+chr(103)+chr(95)+chr(112)+chr(100)+chr(99)+chr(97)]}",
             "", "## Top Agents"]
    for ag, c in st.get("agents",[]): lines.append(f"  - {ag}: {c}")
    lines += ["", "## Top Skills"]
    for sk, c in st.get("skills",[]): lines.append(f"  - {sk}: {c}")
    lines += ["", "## Top Errors"]
    for er, c in st.get("errors",[]): lines.append(f"  - {er}: {c}")
    lines += ["", "## Suggestions"]
    for sg in suggestions(st): lines.append(f"  - {sg}")
    out = Path(f"intelligence/report-{today}.md")
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"Report: {out}")
    update_intel(st)

if __name__ == "__main__": main()
