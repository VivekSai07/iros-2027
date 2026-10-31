import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NODE = ROOT / ".tools/node/node_modules/node/bin/node"


def validate_job_id(name):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Job ID must be YYYY-MM-DD-owner-topic using lowercase letters and digits.")
    datetime.date.fromisoformat(name[:10])


def create_job(parent, name):
    validate_job_id(name)
    job = parent / name
    job.mkdir(parents=True, exist_ok=False)
    return job


def timestamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def write_record(path, record):
    pending = path.with_suffix(path.suffix + ".tmp")
    pending.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    pending.replace(path)


def main():
    parser = argparse.ArgumentParser(description="Run pinned research tools without global configuration changes.")
    parser.add_argument("tool", choices=("feynman", "rea", "obsidian"))
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    environment = os.environ.copy()
    environment["FEYNMAN_TELEMETRY"] = "off"
    environment["CLAUDE_OBSIDIAN_VAULT"] = str(ROOT / "knowledge")
    environment["PATH"] = str(NODE.parent) + os.pathsep + environment.get("PATH", "")
    if args.tool == "obsidian":
        entry = ROOT / ".tools/claude-obsidian/scripts/claude-obsidian.py"
        command = [sys.executable, str(entry), *args.arguments]
    else:
        if not NODE.is_file():
            raise FileNotFoundError("Local Node is missing; run python3 tools/bootstrap.py runtime.")
        package_entry = {
            "feynman": "@companion-ai/feynman/bin/feynman.js",
            "rea": "rea-agents/scripts/rea.mjs",
        }[args.tool]
        entry = ROOT / "tools/node_modules" / package_entry
        command = [str(NODE), str(entry), *args.arguments]
    if not entry.is_file():
        raise FileNotFoundError("Tool is missing; see python3 tools/bootstrap.py --help.")
    if args.tool != "feynman":
        return subprocess.run(command, cwd=ROOT, env=environment).returncode
    if len(args.arguments) < 2:
        raise ValueError("Usage: run_tool.py feynman YYYY-MM-DD-owner-topic <workflow or arguments>")
    job = create_job(ROOT / "knowledge/jobs", args.arguments[0])
    command = [str(NODE), str(entry), *args.arguments[1:]]
    record = {
        "tool": "feynman",
        "command": command[2:],
        "versions": json.loads((ROOT / "tools/package.json").read_text())["dependencies"],
        "code_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "dirty": bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)),
        "started_at": timestamp(),
        "status": "running",
    }
    record_path = job / "job.json"
    write_record(record_path, record)
    try:
        exit_code = subprocess.run(command, cwd=job, env=environment).returncode
    except KeyboardInterrupt:
        exit_code = 130
    record.update({
        "exit_code": exit_code,
        "finished_at": timestamp(),
        "status": "completed" if exit_code == 0 else "failed",
    })
    write_record(record_path, record)
    return exit_code


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, FileExistsError, FileNotFoundError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)