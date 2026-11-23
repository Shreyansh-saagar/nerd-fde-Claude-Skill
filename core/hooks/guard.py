"""nerd-fde PreToolUse guard.

Reads the hook JSON on stdin and prints a permission decision:
  ask  -> git commit, git push
  deny -> force push, rm -rf on broad targets, reading secret files
Anything else, or any internal error, prints nothing and exits 0 (fail open).
"""
import fnmatch
import json
import os
import re
import shlex
import sys

SECRET_GLOBS = (".env", ".env.*", "*.pem", "*.key", "*.p12", "*.pfx", "id_rsa*", "id_ed25519*", "id_ecdsa*")
SECRET_SAFE = (".env.example", ".env.sample", ".env.template", ".env.dist", "*.pub")
READ_CMDS = {"cat", "less", "more", "head", "tail", "bat", "nl", "strings", "xxd", "od", "base64",
             "sed", "awk", "grep", "rg", "cp", "scp", "source", ".", "open", "code", "vim", "vi", "nano"}
SEPARATORS = {";", "&&", "||", "|", "&", "(", ")"}
BROAD_RM = {"/", "/*", "~", "~/", "~/*", "$HOME", "$HOME/", "${HOME}", "*", ".", "./", "..", "../", "./*"}


def is_secret(path):
    name = os.path.basename(path.rstrip("/"))
    if any(fnmatch.fnmatch(name, g) for g in SECRET_SAFE):
        return False
    return any(fnmatch.fnmatch(name, g) for g in SECRET_GLOBS)


def segments(command):
    lex = shlex.shlex(command, posix=True, punctuation_chars=True)
    lex.whitespace_split = True
    seg = []
    for tok in lex:
        if tok in SEPARATORS:
            if seg:
                yield seg
            seg = []
        else:
            seg.append(tok)
    if seg:
        yield seg


def strip_prefix(seg):
    # drop env assignments and wrappers like sudo/env/time so "sudo rm -rf /" is still seen as rm
    while seg and (re.match(r"^\w+=", seg[0]) or seg[0] in {"sudo", "env", "time", "command", "nohup"}):
        seg = seg[1:]
    return seg


def check_git(seg):
    if len(seg) < 2 or os.path.basename(seg[0]) != "git":
        return None
    # skip global options such as -C <dir> or -c k=v
    args = seg[1:]
    while args and args[0].startswith("-"):
        args = args[2:] if args[0] in {"-C", "-c"} else args[1:]
    if not args:
        return None
    sub, rest = args[0], args[1:]
    if sub == "push":
        if any(a in {"-f", "--force"} or a.startswith("--force") or a.startswith("+") for a in rest):
            return ("deny", "Force push is blocked by nerd-fde. Push normally, or run it yourself.")
        return ("ask", "nerd-fde: confirm this git push.")
    if sub == "commit":
        return ("ask", "nerd-fde: confirm this git commit.")
    return None


def check_rm(seg):
    if not seg or os.path.basename(seg[0]) != "rm":
        return None
    flags = "".join(a[1:] for a in seg[1:] if a.startswith("-") and not a.startswith("--"))
    long_flags = {a for a in seg[1:] if a.startswith("--")}
    recursive = "r" in flags or "R" in flags or "--recursive" in long_flags
    force = "f" in flags or "--force" in long_flags
    targets = [a for a in seg[1:] if not a.startswith("-")]
    if recursive and force and any(t in BROAD_RM for t in targets):
        return ("deny", "rm -rf on a broad path (/, ~, *, .) is blocked by nerd-fde.")
    return None


def check_secret_read(seg):
    if not seg or os.path.basename(seg[0]) not in READ_CMDS:
        return None
    if any(is_secret(a) for a in seg[1:] if not a.startswith("-")):
        return ("deny", "Reading secret files (.env, keys) is blocked by nerd-fde. "
                        "Use .env.example or ask the user for the non-secret values you need.")
    return None


def decide(data):
    tool = data.get("tool_name")
    inp = data.get("tool_input") or {}
    if tool == "Read":
        path = inp.get("file_path") or ""
        if is_secret(path):
            return ("deny", "Reading secret files (.env, keys) is blocked by nerd-fde. "
                            "Use .env.example or ask the user for the non-secret values you need.")
        return None
    if tool == "Bash":
        command = inp.get("command") or ""
        result = None
        for seg in segments(command):
            seg = strip_prefix(seg)
            for check in (check_git, check_rm, check_secret_read):
                r = check(seg)
                if r and (result is None or r[0] == "deny"):
                    result = r
            if result and result[0] == "deny":
                break
        return result
    return None


def main():
    try:
        decision = decide(json.load(sys.stdin))
    except Exception:
        return  # fail open: never block work because the guard itself broke
    if decision:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision[0],
            "permissionDecisionReason": decision[1],
        }}))


if __name__ == "__main__":
    main()
