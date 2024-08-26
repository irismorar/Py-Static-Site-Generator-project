import unittest

from  block_to_block_type import block_to_block_type

class Test_block_to_block_type(unittest.TestCase):
  def test_block_to_block_type(self):
    text1 = block_to_block_type("## This is a heading")
    text2 = "heading"
    self.assertEqual(text1, text2)
  
  def test_block_to_block_type(self):
    text1 = block_to_block_type(">This is a quote")
    text2 = "quote"
    self.assertEqual(text1, text2)

  def test_block_to_block_type(self):
    text1 = block_to_block_type("```This is a code block```")
    text2 = "code"
    self.assertEqual(text1, text2)

  def test_block_to_block_type(self):
    text1 = block_to_block_type("This is a code block")
    text2 = "paragraph"
    self.assertEqual(text1, text2)

if __name__ == '__main__':
  unittest.main()