#!/usr/bin/env python3
"""otel-harness.py - OTel-inspired span emitter for ll-vibekit.
Writes .telemetry/sessions/{id}.json (local only, gitignored).
Usage:
  python3 scripts/otel-harness.py start PROJECT TASK
  python3 scripts/otel-harness.py end SESSION_ID outcome
  python3 scripts/otel-harness.py span SESSION_ID span_type data
  python3 scripts/otel-harness.py error SESSION_ID error_type message
"""
import sys, json, datetime, uuid
from pathlib import Path

TELEMETRY = Path(".telemetry/sessions")

def now(): return datetime.datetime.utcnow().isoformat() + "Z"
def sf(sid): TELEMETRY.mkdir(parents=True, exist_ok=True); return TELEMETRY / f"{sid}.json"
def load(sid): f = sf(sid); return json.loads(f.read_text()) if f.exists() else {}
def save(sid, d): sf(sid).write_text(json.dumps(d, indent=2))

def cmd_start(project, task):
    sid = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    save(sid, {"session_id": sid, "project_name": project,
        "task_description": task, "started_at": now(),
        "spans": [], "errors": [], "agents_used": [], "skills_used": [],
        "new_patterns": [], "new_mistakes": [],
        "pdca_iterations": 0, "prp_generated": False,
        "feature_shipped": False, "tokens_estimated": 0, "outcome": "in-progress"})
    print(sid)

def cmd_span(sid, stype, sdata):
    d = load(sid)
    if not d: return
    if stype == "agent_activated" and sdata not in d["agents_used"]: d["agents_used"].append(sdata)
    if stype == "skill_used" and sdata not in d["skills_used"]: d["skills_used"].append(sdata)
    if stype == "prp_generated": d["prp_generated"] = True
    if stype == "pdca_iteration": d["pdca_iterations"] += 1
    if stype == "feature_shipped": d["feature_shipped"] = True; d["outcome"] = "shipped"
    if stype == "pattern_discovered": d["new_patterns"].append(sdata)
    d.setdefault("spans", []).append({"span_id": str(uuid.uuid4())[:8],
        "span_type": stype, "timestamp": now(), "data": sdata})
    save(sid, d)

def cmd_error(sid, etype, msg):
    d = load(sid)
    if not d: return
    d.setdefault("errors", []).append({"type": etype, "message": msg,
        "timestamp": now(), "resolved": False})
    save(sid, d)

def cmd_end(sid, outcome):
    d = load(sid)
    if not d: return
    d["ended_at"] = now(); d["outcome"] = outcome
    if "started_at" in d:
        s = datetime.datetime.fromisoformat(d["started_at"].rstrip("Z"))
        e = datetime.datetime.fromisoformat(d["ended_at"].rstrip("Z"))
        d["duration_minutes"] = round((e-s).total_seconds()/60, 1)
    save(sid, d)
    print(f"Session {sid} ended: {outcome} ({d.get(chr(100)+chr(117)+chr(114)+chr(97)+chr(116)+chr(105)+chr(111)+chr(110)+chr(95)+chr(109)+chr(105)+chr(110)+chr(117)+chr(116)+chr(101)+chr(115),chr(63))}min)")

cmds = {"start": lambda a: cmd_start(a[0]," ".join(a[1:])),
        "end": lambda a: cmd_end(a[0],a[1]),
        "span": lambda a: cmd_span(a[0],a[1]," ".join(a[2:])),
        "error": lambda a: cmd_error(a[0],a[1]," ".join(a[2:]))}

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: otel-harness.py <start|end|span|error> [args]"); sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    cmds.get(cmd, lambda a: print(f"Unknown: {cmd}"))(args)
