import unittest

from markdown_to_blocks import markdown_to_blocks

class Test_markdown_to_blocks(unittest.TestCase):
  def test_blocks(self):
    text1 = markdown_to_blocks("blabla.\n\nhghghghghghhg.\n\niiiiii\nooooo\npppppppp\n")
    text2 = ['blabla.', 'hghghghghghhg.', 'iiiiii\nooooo\npppppppp']
    self.assertEqual(text1, text2)

  def test_blocks2(self):
    text1 = markdown_to_blocks("# This is a heading\n\n       This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n     * This is another list item\n\n")
    text2 = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
    self.assertEqual(text1, text2)

if __name__ == '__main__':
  unittest.main()