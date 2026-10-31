import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from check_commit_message import ATTRIBUTION


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description="Offline checks for local document targets, JSON, pins, and shared entry points.")
    parser.add_argument("--commit-range", help="Also check commit messages in this Git revision range.")
    args = parser.parse_args()
    errors = []
    files = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    ).decode().split("\0")
    for relative in sorted(set(files) - {""}):
        path = ROOT / relative
        if not path.is_file():
            continue
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as error:
                errors.append(f"{relative}: invalid JSON: {error}")
        if path.suffix != ".md":
            continue
        if relative.startswith("knowledge/") and relative != "knowledge/index.md" and not relative.startswith("knowledge/wiki/"):
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"{relative}: missing or external local target {target}")
    for required in ("AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md", "knowledge/index.md", "tools/package-lock.json"):
        if not (ROOT / required).is_file():
            errors.append(f"Missing required entry: {required}")
    canonical = ROOT / ".agents/skills/research-workflow/SKILL.md"
    for adapter in (".claude/skills/research-workflow/SKILL.md", ".github/skills/research-workflow/SKILL.md"):
        path = ROOT / adapter
        if not path.is_file() or not canonical.is_file() or not path.samefile(canonical):
            errors.append(f"{adapter}: must resolve to the canonical research skill")
    package = json.loads((ROOT / "tools/package.json").read_text())
    lock_path = ROOT / "tools/package-lock.json"
    if lock_path.is_file():
        lock = json.loads(lock_path.read_text())
        if lock["packages"][""]["dependencies"] != package["dependencies"]:
            errors.append("CLI lockfile and dependency manifest differ")
    for name, source in json.loads((ROOT / "tools/upstreams.json").read_text()).items():
        if not re.fullmatch(r"[0-9a-f]{40}", source["revision"]):
            errors.append(f"{name}: source must use a full immutable Git revision")
    if args.commit_range:
        commits = subprocess.check_output(["git", "rev-list", args.commit_range], cwd=ROOT, text=True).splitlines()
        for commit in commits:
            message = subprocess.check_output(["git", "show", "-s", "--format=%B", commit], cwd=ROOT, text=True)
            if ATTRIBUTION.search(message):
                errors.append(f"{commit}: commit message contains AI attribution or branding")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository checks passed: local document targets, JSON, source pins, CLI lock, and shared entry points.")
    print("Historical research links, remote URLs, Markdown anchors, secrets, and live client loading are not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())