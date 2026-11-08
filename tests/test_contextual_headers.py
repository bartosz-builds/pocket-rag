import unittest

from pocket_rag.file.handler import _extract_heading


class TestExtractHeading(unittest.TestCase):
    def test_title_case_heading(self):
        text = "Introduction\nSome body text that follows the heading."
        self.assertEqual(_extract_heading(text), "Introduction")

    def test_all_caps_heading(self):
        text = "CHAPTER 1\nContent here about the chapter."
        self.assertEqual(_extract_heading(text), "CHAPTER 1")

    def test_markdown_heading(self):
        text = "# Overview\nDetails about the project."
        self.assertEqual(_extract_heading(text), "Overview")

    def test_multi_hash_markdown_heading(self):
        text = "## Getting Started\nFirst install the package."
        self.assertEqual(_extract_heading(text), "Getting Started")

    def test_no_heading_found(self):
        text = "just some regular lowercase text\nmore lowercase text here"
        self.assertIsNone(_extract_heading(text))

    def test_long_line_skipped(self):
        long = "A" * 121
        text = f"{long}\nReal Heading\nBody text."
        self.assertEqual(_extract_heading(text), "Real Heading")

    def test_empty_text(self):
        self.assertIsNone(_extract_heading(""))

    def test_only_whitespace_lines(self):
        self.assertIsNone(_extract_heading("   \n  \n   "))

    def test_skips_empty_lines_before_heading(self):
        text = "\n\n  \nConfiguration\nSet the following values..."
        self.assertEqual(_extract_heading(text), "Configuration")


if __name__ == "__main__":
    unittest.main()
