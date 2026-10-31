import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.run_tool import create_job, validate_job_id, write_record


class ToolRunnerTests(unittest.TestCase):
    def test_rejects_paths_and_ambiguous_job_names(self):
        for name in ("../outside", "/tmp/job", "topic", "2026-10-31-../outside", "2026-10-31-Topic"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_job_id(name)

    def test_job_stays_under_selected_root(self):
        with tempfile.TemporaryDirectory() as directory:
            job = create_job(Path(directory), "2026-10-31-owner-gap-check")
            self.assertEqual(job, Path(directory) / "2026-10-31-owner-gap-check")
            self.assertTrue(job.is_dir())

    def test_refuses_to_overwrite_an_existing_job(self):
        with tempfile.TemporaryDirectory() as directory:
            create_job(Path(directory), "2026-10-31-owner-gap-check")
            with self.assertRaises(FileExistsError):
                create_job(Path(directory), "2026-10-31-owner-gap-check")

    def test_rejects_impossible_dates(self):
        with self.assertRaises(ValueError):
            validate_job_id("2026-02-31-owner-topic")

    def test_record_replacement_preserves_valid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "job.json"
            write_record(path, {"status": "running"})
            write_record(path, {"status": "completed", "exit_code": 0})
            self.assertEqual(json.loads(path.read_text()), {"status": "completed", "exit_code": 0})

    def test_failed_atomic_replace_preserves_previous_record(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "job.json"
            path.write_text('{"status": "running"}\n', encoding="utf-8")
            with patch("tools.run_tool.Path.replace", side_effect=OSError("disk error")):
                with self.assertRaises(OSError):
                    write_record(path, {"status": "completed"})
            self.assertEqual(json.loads(path.read_text()), {"status": "running"})


if __name__ == "__main__":
    unittest.main()