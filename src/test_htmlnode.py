import unittest

from html_node import HTMLNode
from html_node import LeafNode
from html_node import ParentNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode(tag="a", props={'href': 'https://example.com', 'target': '_blank'})
    expected_props = "href='https://example.com' target='_blank'"
    self.assertEqual(node.props_to_html(), expected_props)
  def test_props_to_html(self):
     node = HTMLNode(tag='p', props={'color': '#00FF00', 'text-align': 'center'})
     expected_props = "color='#00FF00' text-aligggn='center'"
     self.assertNotEqual(node.props_to_html(), expected_props)
  def test_props_to_html(self):
     node = HTMLNode(tag='h1', props={'font-size': '4em', 'border': '5px solid purple'})
     expected_props = "font-size='4rem' border='5px solid purple'"
     self.assertNotEqual(node.props_to_html(), expected_props)
  def test_props_to_html(self):
     node = HTMLNode(tag='ol', props={})
     expected_props = ''
     self.assertEqual(node.props_to_html(), expected_props)
  def test_props_to_html(self):
     node = HTMLNode(tag='a', props=None)
     expected_props = ''
     self.assertEqual(node.props_to_html(), expected_props)

class TestLeafNode(unittest.TestCase):
   def test_to_html(self):
      node = LeafNode(tag="p", value="This is a paragraph of text.")
      expected_text = "<p>This is a paragraph of text.</p>"
      self.assertEqual(node.to_html(), expected_text)
   def test_to_html(self):
      node = LeafNode(tag="a", value="Click me!", props={'href': 'https://www.youtube.com'})
      expected_text = "<a href='https://www.youtube.com'>Click me!</a>"
      self.assertEqual(node.to_html(), expected_text)

class TestParentNode(unittest.TestCase):
   def test_to_html(self):
      node = ParentNode(
         "p",
         [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
         ],
      )
      expected_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
      self.assertEqual(node.to_html(), expected_output)
   def test_to_html(self):
      node = ParentNode("ul", [LeafNode("li", "first list element"), LeafNode("li", "second list element")])
      expected_output = "<ul><li>first list element</li><li>second list element</li></ul>"
      self.assertEqual(node.to_html(), expected_output)
   def test_to_html(self):
      node = ParentNode("span", [])
      with self.assertRaises(ValueError) as context:
        node.to_html()
      self.assertEqual(str(context.exception), "You must enter at least one child")

if __name__ == "__main__":
    unittest.main()