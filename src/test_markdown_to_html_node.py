import unittest

from markdown_to_html_node import markdown_to_html_node

class Test_markdown_to_html_node(unittest.TestCase):
  def test_plm(self):
    markdown = "## This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n>And here is a quote.\n\n```print('Do it!')```\n\n>And here another quote.\n\n* This is the first list item in an unordered list block\n* This is a list item\n* This is another list item\n\nNow we are going to create an ordered list:\n\n1. This is the first item in that ordered list block\n 2. And this is the second item of it."
    html = "<div><h2>This is a heading</h2><p>This is a paragraph of text. It has some **bold** and *italic* words inside of it.</p><blockquote>And here is a quote.</blockquote><pre><code>print('Do it!')</code></pre><blockquote>And here another quote.</blockquote><ul><li>This is the first list item in an unordered list block</li><li>This is a list item</li><li>This is another list item</li></ul><p>Now we are going to create an ordered list:</p><ol><li>This is the first item in that ordered list block</li><li>And this is the second item of it.</li></ol></div>"
    self.assertEqual(markdown_to_html_node(markdown), html)

if __name__ == '__main__':
  unittest.main()