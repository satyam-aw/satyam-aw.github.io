"""Offline checks for preserving citation data when Scholar or file writes fail."""
import contextlib
import io
import os
from pathlib import Path
import runpy
import sys
import tempfile
import types
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

import yaml

SCRIPT = Path(__file__).resolve().parents[1] / "bin/update_scholar_citations.py"


class CitationRefreshTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        previous = os.getcwd()
        os.chdir(self.directory.name)
        self.addCleanup(os.chdir, previous)
        Path("_data").mkdir()
        Path("_data/socials.yml").write_text("scholar_userid: test-author\n")
        self.path = Path("_data/citations.yml")
        self.saved = {"metadata": {"last_updated": "2000-01-01"}, "papers": {"test:paper": {"title": "Paper", "year": "2024", "citations": 3}}}
        self.path.write_text(yaml.safe_dump(self.saved))
        self.original = self.path.read_bytes()
        self.scholar = MagicMock()
        module = types.ModuleType("scholarly")
        module.scholarly = self.scholar
        with patch.dict(sys.modules, {"scholarly": module}):
            self.refresh = runpy.run_path(str(SCRIPT))["get_scholar_citations"]
        self.scholar.fill.return_value = {"publications": [{"author_pub_id": "test:paper", "bib": {"title": "Paper", "pub_year": "2024"}, "num_citations": 3}]}
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_success_records_check_even_when_counts_unchanged(self):
        self.refresh()
        data = yaml.safe_load(self.path.read_text())
        self.assertEqual(data["metadata"]["last_updated"], datetime.now().strftime("%Y-%m-%d"))
        self.assertEqual(data["papers"], self.saved["papers"])
        self.scholar.fill.assert_called_once_with(self.scholar.search_author_id.return_value, sections=["publications"])

    def test_fetch_failure_preserves_saved_bytes(self):
        self.scholar.search_author_id.side_effect = RuntimeError("blocked")
        with self.assertRaises(SystemExit):
            self.refresh()
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_empty_response_preserves_saved_bytes(self):
        self.scholar.fill.return_value = {"publications": []}
        with self.assertRaises(SystemExit):
            self.refresh()
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_invalid_or_missing_counts_and_ids_preserve_data(self):
        for change in ({"num_citations": -1}, {"num_citations": True}, {"num_citations": "4"}, {"author_pub_id": None}):
            with self.subTest(change=change):
                pub = {"author_pub_id": "test:paper", "num_citations": 4, "bib": {"title": "Paper"}}
                pub.update(change)
                self.scholar.fill.return_value = {"publications": [pub]}
                with self.assertRaises(ValueError):
                    self.refresh()
                self.assertEqual(self.path.read_bytes(), self.original)
        self.scholar.fill.return_value = {"publications": [{"author_pub_id": "test:paper", "bib": {"title": "Paper"}}]}
        with self.assertRaises(KeyError):
            self.refresh()
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_failed_replace_preserves_data_and_removes_temporary_file(self):
        with patch("os.replace", side_effect=OSError("read only")):
            with self.assertRaises(SystemExit):
                self.refresh()
        self.assertEqual(self.path.read_bytes(), self.original)
        self.assertEqual(list(Path("_data").glob("*.tmp")), [])

    def test_missing_output_file_can_be_created(self):
        self.path.unlink()
        self.refresh()
        self.assertIn("test:paper", yaml.safe_load(self.path.read_text())["papers"])

    def test_same_day_check_skips_network(self):
        self.saved["metadata"]["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        self.path.write_text(yaml.safe_dump(self.saved))
        self.refresh()
        self.scholar.search_author_id.assert_not_called()


if __name__ == "__main__":
    unittest.main()
