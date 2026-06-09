#!/usr/bin/env python3
"""eval-session.py -- Score a vibe coding session and update MEMORY/.
Usage:
    python3 scripts/eval-session.py           # eval latest session
    python3 scripts/eval-session.py --summary # show all stats
"""
import sys, json, datetime, re
from pathlib import Path

TELEMETRY = Path(".telemetry/sessions")
MEMORY = Path("MEMORY")
INTEL = Path("intelligence/INTELLIGENCE.md")

def load_session(sid=None):
    TELEMETRY.mkdir(parents=True, exist_ok=True)
    files = sorted(TELEMETRY.glob("*.json"), reverse=True)
    if not files: return None
    if sid:
        for f in files:
            if sid in f.name: return json.loads(f.read_text())
        return None
    return json.loads(files[0].read_text())

def score_session(s):
    score, notes = 0, []
    if s.get("prp_generated"): score += 20
    else: notes.append("No PRP generated")
    if s.get("feature_shipped"): score += 30
    else: notes.append("Feature not shipped")
    iters = s.get("pdca_iterations", 0)
    if iters == 1: score += 30; notes.append("PDCA passed first time")
    elif iters <= 2: score += 20; notes.append(f"PDCA passed in {iters} iterations")
    elif iters <= 4: score += 10; notes.append(f"PDCA needed {iters} iterations")
    else: notes.append(f"PDCA needed {iters}+ iterations -- review approach")
    errors = s.get("errors", [])
    unresolved = [e for e in errors if not e.get("resolved")]
    if not errors: score += 20
    elif not unresolved: score += 10; notes.append(f"{len(errors)} errors resolved")
    else: notes.append(f"{len(unresolved)} unresolved errors")
    return min(score, 100), notes

def update_memory(s):
    today = datetime.date.today().isoformat()
    patterns = s.get("new_patterns", [])
    mistakes = s.get("new_mistakes", []) + [e["message"] for e in s.get("errors",[]) if not e.get("resolved")]
    if patterns:
        pf = MEMORY / "patterns.md"
        if pf.exists():
            existing = pf.read_text()
            add = f"\n\n## {today} (session: {s[chr(115)+chr(101)+chr(115)+chr(115)+chr(105)+chr(111)+chr(110)+chr(95)+chr(105)+chr(100)]})" + "".join(f"\n- {p}" for p in patterns)
            pf.write_text(existing + add)
            print(f"  Updated MEMORY/patterns.md (+{len(patterns)})")
    if mistakes:
        mf = MEMORY / "mistakes.md"
        if mf.exists():
            existing = mf.read_text()
            add = f"\n\n## {today}\n" + "".join(f"\n- {m}" for m in mistakes)
            mf.write_text(existing + add)
            print(f"  Updated MEMORY/mistakes.md (+{len(mistakes)})")

def update_intel(s, score, notes):
    if not INTEL.exists(): return
    today = datetime.date.today().isoformat()
    entry = f"\n\n## {s[chr(115)+chr(101)+chr(115)+chr(115)+chr(105)+chr(111)+chr(110)+chr(95)+chr(105)+chr(100)]} | {today} | {score}/100 | {s.get(chr(111)+chr(117)+chr(116)+chr(99)+chr(111)+chr(109)+chr(101),chr(63))}\n"
    entry += f"Task: {s.get(chr(116)+chr(97)+chr(115)+chr(107)+chr(95)+chr(100)+chr(101)+chr(115)+chr(99)+chr(114)+chr(105)+chr(112)+chr(116)+chr(105)+chr(111)+chr(110),chr(45))}\n"
    entry += "\n".join(f"  - {n}" for n in notes) + "\n"
    INTEL.write_text(INTEL.read_text() + entry)
    print(f"  Updated intelligence/INTELLIGENCE.md")

def show_summary():
    TELEMETRY.mkdir(parents=True, exist_ok=True)
    sessions = [json.loads(f.read_text()) for f in TELEMETRY.glob("*.json")]
    if not sessions: print("No sessions yet."); return
    total = len(sessions)
    shipped = sum(1 for s in sessions if s.get("feature_shipped"))
    avg_iters = sum(s.get("pdca_iterations",0) for s in sessions) / total
    print(f"Sessions: {total} | Shipped: {shipped} | Avg PDCA: {avg_iters:.1f}")

def main():
    if "--summary" in sys.argv: show_summary(); return
    sid = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    s = load_session(sid)
    if not s: print("No session data. Sessions created by hooks/session-end.sh."); return
    score, notes = score_session(s)
    print(f"Session: {s.get(chr(115)+chr(101)+chr(115)+chr(115)+chr(105)+chr(111)+chr(110)+chr(95)+chr(105)+chr(100))} | Score: {score}/100")
    for n in notes: print(f"  - {n}")
    update_memory(s)
    update_intel(s, score, notes)

if __name__ == "__main__": main()
