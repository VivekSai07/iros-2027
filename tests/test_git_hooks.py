import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GitHookTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.repo = Path(self.directory.name)
        self.env = os.environ.copy()
        for key in list(self.env):
            if key.startswith("GIT_") or key == "RESEARCH_HUMAN_PUSH":
                self.env.pop(key)
        self.env.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_AUTHOR_NAME": "Test Researcher",
            "GIT_AUTHOR_EMAIL": "researcher@example.org",
            "GIT_COMMITTER_NAME": "Test Researcher",
            "GIT_COMMITTER_EMAIL": "researcher@example.org",
        })
        self.git("init", "-b", "main")
        self.git("-c", "core.hooksPath=" + os.devnull, "commit", "--allow-empty", "-m", "Initial state")
        self.git("config", "core.hooksPath", str(ROOT / ".githooks"))

    def git(self, *args, check=True):
        return subprocess.run(
            ["git", *args], cwd=self.repo, env=self.env,
            capture_output=True, text=True, check=check,
        )

    def test_blocks_direct_main_commit(self):
        result = self.git("commit", "--allow-empty", "-m", "docs: update protocol", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("topic branch", result.stderr)

    def test_allows_topic_branch_commit(self):
        self.git("switch", "-c", "feature/test", "main")
        result = self.git("commit", "--allow-empty", "-m", "docs: update protocol", check=False)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_attribution_through_git(self):
        self.git("switch", "-c", "feature/test", "main")
        result = self.git("commit", "--allow-empty", "-m", "docs: update with Copilot", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("attribution", result.stderr)

    def test_non_fast_forward_merge_has_two_parents(self):
        self.git("switch", "-c", "feature/test", "main")
        self.git("commit", "--allow-empty", "-m", "docs: update protocol")
        self.git("switch", "main")
        self.git("merge", "--no-ff", "-m", "Merge feature/test", "feature/test")
        parents = self.git("rev-list", "--parents", "-n", "1", "HEAD").stdout.split()
        self.assertEqual(len(parents), 3)

    def test_push_hook_requires_manual_override(self):
        result = subprocess.run(
            ["bash", str(ROOT / ".githooks/pre-push")],
            env=self.env, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("human", result.stderr.lower())
        result = subprocess.run(
            ["bash", str(ROOT / ".githooks/pre-push")],
            env={**self.env, "RESEARCH_HUMAN_PUSH": "1"},
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()