import unittest

from gencontent import extract_title


class TestExtractionMethods(unittest.TestCase):
    def test_title_extraction(self):
        title = "# This is a title"
        assert extract_title(title) == "This is a title"

    def test_no_title_extraction_exception(self):
        title = "This is not a title"
        try:
            extract_title(title)
            assert False
        except Exception:
            assert True

    def test_multiple_hashes_in_title(self):
        title = "## This is not a title"
        try:
            extract_title(title)
            assert False
        except Exception:
            assert True

    def test_extra_spaces_between(self):
        title = "#     Title with spaces"
        assert extract_title(title) == "Title with spaces"

    def test_only_h2_and_h3_raises(self):
        title = "## heading\n### subheading"
        try:
            extract_title(title)
            assert False
        except Exception:
            assert True

    def test_eq_double(self):
        title = extract_title(
        """
# This is a title
        
# this is ignored
"""
        )
        self.assertEqual(title, "This is a title")

if __name__ == "__main__":
    unittest.main()