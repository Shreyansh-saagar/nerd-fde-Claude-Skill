"""Run: python3 -I core/hooks/test_guard.py  (no dependencies)"""
import json
import os
import subprocess
import sys

GUARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard.py")


def run(payload):
    raw = payload if isinstance(payload, str) else json.dumps(payload)
    p = subprocess.run([sys.executable, "-I", GUARD], input=raw, capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    return json.loads(p.stdout)["hookSpecificOutput"]["permissionDecision"] if p.stdout.strip() else None


def bash(cmd):
    return run({"tool_name": "Bash", "tool_input": {"command": cmd}})


def read(path):
    return run({"tool_name": "Read", "tool_input": {"file_path": path}})


CASES = [
    # (description, actual, expected)
    ("plain commit asks", lambda: bash('git commit -m "x"'), "ask"),
    ("commit in chain asks", lambda: bash("git add -A && git commit -m x"), "ask"),
    ("git -C dir commit asks", lambda: bash("git -C /tmp/r commit -m x"), "ask"),
    ("push asks", lambda: bash("git push origin main"), "ask"),
    ("force push denied", lambda: bash("git push --force origin main"), "deny"),
    ("-f push denied", lambda: bash("git push -f"), "deny"),
    ("lease push denied", lambda: bash("git push --force-with-lease"), "deny"),
    ("+refspec push denied", lambda: bash("git push origin +main"), "deny"),
    ("commit then force push denied", lambda: bash("git commit -m x && git push -f"), "deny"),
    ("git status allowed", lambda: bash("git status"), None),
    ("git log allowed", lambda: bash("git log --oneline | head"), None),
    ("rm -rf / denied", lambda: bash("rm -rf /"), "deny"),
    ("sudo rm -fr ~ denied", lambda: bash("sudo rm -fr ~"), "deny"),
    ("rm -r -f * denied", lambda: bash("rm -r -f *"), "deny"),
    ("rm --recursive --force . denied", lambda: bash("rm --recursive --force ."), "deny"),
    ("rm -rf node_modules allowed", lambda: bash("rm -rf node_modules"), None),
    ("rm file allowed", lambda: bash("rm build.log"), None),
    ("cat .env denied", lambda: bash("cat .env"), "deny"),
    ("cat backend/.env.local denied", lambda: bash("cat backend/.env.local"), "deny"),
    ("grep in .env denied", lambda: bash("grep KEY .env"), "deny"),
    ("cat id_rsa denied", lambda: bash("cat ~/.ssh/id_rsa"), "deny"),
    ("cat .env.example allowed", lambda: bash("cat .env.example"), None),
    ("cat id_rsa.pub allowed", lambda: bash("cat ~/.ssh/id_rsa.pub"), None),
    ("ls .env allowed", lambda: bash("ls -la .env"), None),
    ("docker --env-file allowed", lambda: bash("docker compose --env-file .env up -d"), None),
    ("Read .env denied", lambda: read("/repo/.env"), "deny"),
    ("Read server.key denied", lambda: read("/repo/certs/server.key"), "deny"),
    ("Read .env.sample allowed", lambda: read("/repo/.env.sample"), None),
    ("Read normal file allowed", lambda: read("/repo/src/app.ts"), None),
    ("other tool ignored", lambda: run({"tool_name": "Edit", "tool_input": {"file_path": ".env"}}), None),
    ("bad json fails open", lambda: run("not json"), None),
    ("unbalanced quote fails open", lambda: bash('echo "unterminated'), None),
]

failed = 0
for name, fn, expected in CASES:
    got = fn()
    ok = got == expected
    failed += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}  (got {got}, expected {expected})")
print(f"\n{len(CASES) - failed}/{len(CASES)} passed")
sys.exit(1 if failed else 0)
