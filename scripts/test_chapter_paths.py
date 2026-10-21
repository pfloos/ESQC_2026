"""Regression tests for minimal, comment-aware chapter graphic discovery."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import chapter_paths


class RequiredAssetsTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "figures").mkdir()
        self.override = patch.object(chapter_paths, "CHAPTER", self.root)
        self.override.start()
        self.addCleanup(self.override.stop)

    def source(self, text):
        (self.root / f"{chapter_paths.STEM}.tex").write_text(text)

    def asset(self, name):
        target = self.root / "figures" / name
        target.touch()
        return target

    def test_ignores_commented_book_covers(self):
        kept = self.asset("kept.png")
        self.source("%\\includegraphics{Jensen}\n"
                    "\\includegraphics{kept} %\\includegraphics{Cramer}\n")
        self.assertEqual(chapter_paths.required_assets(), [kept])

    def test_escaped_percent_does_not_start_comment(self):
        kept = self.asset("kept.png")
        self.source(r"50\% text \includegraphics{kept}")
        self.assertEqual(chapter_paths.required_assets(), [kept])

    def test_resolves_portrait_macro_arguments_once(self):
        portrait = self.asset("sketch-example.png")
        self.source(r"\includegraphics[height=27mm]{#1}" + "\n"
                    + r"\hfbiophoto{figures/sketch-example.png}" + "\n"
                    + r"\hfbiophoto{figures/sketch-example.png}")
        self.assertEqual(chapter_paths.required_assets(), [portrait])

    def test_rejects_missing_active_asset(self):
        self.source(r"\includegraphics{missing}")
        with self.assertRaisesRegex(ValueError, "missing graphic"):
            chapter_paths.required_assets()

    def test_rejects_ambiguous_extension(self):
        self.asset("ambiguous.png")
        self.asset("ambiguous.pdf")
        self.source(r"\includegraphics{ambiguous}")
        with self.assertRaisesRegex(ValueError, "Ambiguous"):
            chapter_paths.required_assets()


if __name__ == "__main__":
    unittest.main()
