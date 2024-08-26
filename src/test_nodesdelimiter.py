import unittest

from nodesdelimiter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes,
)

from text_node import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_image,
    text_type_link,
    text_type_code,
)

class Testnodesdelimiter(unittest.TestCase):
  def test_delimiter_bold(self):
    node = TextNode("This is a place where **somebody** knows **me**", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertListEqual(
      [
        TextNode("This is a place where ", text_type_text),
        TextNode("somebody", text_type_bold),
        TextNode(" knows ", text_type_text),
        TextNode("me", text_type_bold),
      ],
      new_nodes
    )
  
  def test_unclosed_delimiter_italic(self):
    node = TextNode("This is an *italic word", text_type_text)
    with self.assertRaises(ValueError) as context:
        split_nodes_delimiter([node], "*", text_type_italic)

    self.assertTrue("invalid Markdown syntax" in str(context.exception))

  def test_extract_markdown_images(self):
    example = extract_markdown_images("This is text with an ![my_image](https://i.imgur.com/zjjcJKZ.png)")
    self.assertEqual([("my_image", "https://i.imgur.com/zjjcJKZ.png")], example)

  def test_example_markdown_images(self):
    example = extract_markdown_images("This is a text with this image ![first_image](https://google.com/zjjcJKZ.png) and this image ![second_image](https://pixar.com/zjjcJKZ.jpg)")
    self.assertNotEqual(
      [("first_image", "https://google.com/zjjcJKZ.png"), 
       ("second_image", "pixar.com/zjjcJKZ.jpg")], 
      example
    )

  def test_extract_markdown_links(self):
    example = extract_markdown_links("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)")
    self.assertEqual(
      [("link","https://boot.dev"),
       ("another link","https://blog.boot.dev")],
      example
    )

  def test_split_image(self):
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", text_type_text)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", text_type_text),
        TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
      ],
      new_nodes,
    )

  def test_split_image_single(self):
    node = TextNode("![image](https://www.example.com/image.png)", text_type_text)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("image", text_type_image, "https://www.example.com/image.png"),
      ],
      new_nodes,
    )


  def test_split_links(self):
    node = TextNode("This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows", text_type_text)
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      [
        TextNode("This is text with a ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev"),
        TextNode(" and ", text_type_text),
        TextNode("another link", text_type_link, "https://blog.boot.dev"),
        TextNode(" with text that follows", text_type_text),
      ],
      new_nodes,
    )


  def test_text_to_textnodes(self):
    nodes = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
    self.assertListEqual(
      [
        TextNode("This is ", text_type_text),
        TextNode("text", text_type_bold),
        TextNode(" with an ", text_type_text),
        TextNode("italic", text_type_italic),
        TextNode(" word and a ", text_type_text),
        TextNode("code block", text_type_code),
        TextNode(" and an ", text_type_text),
        TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and a ", text_type_text),
        TextNode("link", text_type_link, "https://boot.dev"),
      ],
      nodes,
    )



if __name__ == '__main__':
  unittest.main()