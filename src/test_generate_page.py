import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        title = extract_title("# This is a title")
        self.assertEqual(title, "This is a title")
    def test_title2(self):
       title = extract_title(
      """
# This is a title

# This is a second title that should be ignored
"""
       )
       self.assertEqual(title, "This is a title")
    def test_title3(self):
          try:
            extract_title("there is no title")
            self.fail("No title found")
          except Exception as e:
            pass

if __name__ == "__main__":
  unittest.main()
