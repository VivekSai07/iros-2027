import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPSTREAMS = json.loads((ROOT / "tools/upstreams.json").read_text(encoding="utf-8"))
PACKAGE = json.loads((ROOT / "tools/package.json").read_text(encoding="utf-8"))
NODE = ROOT / ".tools/node/node_modules/node/bin/node"


def run(*command, **kwargs):
    subprocess.run(command, cwd=ROOT, check=True, **kwargs)


def source_ready(name, specification):
    path = ROOT / ".tools" / name
    if not (path / ".git").is_dir():
        return False
    revision = subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()
    clean = subprocess.run(["git", "-C", str(path), "diff", "--quiet", "HEAD"]).returncode == 0
    return revision == specification["revision"] and clean


def sources():
    for name, specification in UPSTREAMS.items():
        path = ROOT / ".tools" / name
        if path.exists():
            if not source_ready(name, specification):
                raise ValueError(f"{path} exists but is incomplete, modified, or at another revision; inspect it manually.")
            continue
        run("git", "init", str(path))
        run("git", "-C", str(path), "remote", "add", "origin", specification["url"])
        run("git", "-C", str(path), "fetch", "--depth", "1", "origin", specification["revision"])
        run("git", "-C", str(path), "checkout", "--detach", "FETCH_HEAD")
        if not source_ready(name, specification):
            raise ValueError(f"Revision verification failed for {name}.")
        print(f"Ready: {name}@{specification['revision']}", flush=True)


def runtime():
    version = PACKAGE["engines"]["node"]
    if not NODE.exists():
        run("npm", "install", "--prefix", str(ROOT / ".tools/node"), "--save-exact", "--no-fund", f"node@{version}")
    actual = subprocess.check_output([str(NODE), "--version"], text=True).strip()
    if actual != "v" + version:
        raise ValueError(f"Local Node is {actual}, expected v{version}; inspect .tools/node before updating.")
    environment = os.environ.copy()
    environment["PATH"] = str(NODE.parent) + os.pathsep + environment.get("PATH", "")
    environment["FEYNMAN_TELEMETRY"] = "off"
    run("npm", "--prefix", "tools", "ci", "--engine-strict", "--no-fund", env=environment)


def check():
    ready = True
    for name, specification in UPSTREAMS.items():
        present = source_ready(name, specification)
        print(f"{name}: {'ready at pinned revision' if present else 'missing or changed'}")
        ready = ready and present
    node_ready = NODE.is_file() and subprocess.check_output([str(NODE), "--version"], text=True).strip() == "v" + PACKAGE["engines"]["node"]
    print(f"Node {PACKAGE['engines']['node']}: {'ready' if node_ready else 'missing or changed'}")
    ready = ready and node_ready
    for name, version in PACKAGE["dependencies"].items():
        manifest = ROOT / "tools/node_modules" / name / "package.json"
        present = manifest.is_file() and json.loads(manifest.read_text(encoding="utf-8"))["version"] == version
        print(f"{name}@{version}: {'installed' if present else 'missing or changed'}")
        ready = ready and present
    print("This checks local files and versions, not authentication, client discovery, or native-analysis providers.")
    return 0 if ready else 1


def main():
    parser = argparse.ArgumentParser(description="Opt-in local tool setup; check performs no downloads or writes.")
    parser.add_argument("action", choices=("sources", "runtime", "check"))
    parser.add_argument("--accept-upstream-risk", action="store_true", help="Human-reviewed exception for the dependency advisories documented in tools/README.md.")
    args = parser.parse_args()
    if args.action == "sources":
        sources()
    elif args.action == "runtime":
        if not args.accept_upstream_risk:
            raise ValueError("CLI activation is gated by upstream dependency advisories. Read tools/README.md; obtain human approval before --accept-upstream-risk.")
        runtime()
    else:
        return check()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"Setup stopped: {error}", file=sys.stderr)
        raise SystemExit(1)