from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from html_node import (LeafNode,ParentNode)


def markdown_to_html_node(markdown):
  html_blocks = []
  blocks = markdown_to_blocks(markdown)
  for block in blocks:
    type = block_to_block_type(block)
    if type == 'heading':
      splitted_block = block.split(" ")
      tag_name = f"h{len(splitted_block[0])}"
      joined_block = " ".join(splitted_block[1:])
      node = LeafNode(tag=tag_name, value=joined_block)
      node_to_html = node.to_html()
      html_blocks.append(node_to_html)
    if type == 'code':
      replaced_block = block.replace("```", "")
      node = ParentNode("pre", [LeafNode("code", value=replaced_block)])
      node_to_html = node.to_html()
      html_blocks.append(node_to_html)
    if type == 'unordered_list':
      splitted_block = block.split("\n")
      leaf_nodes = list(map(lambda unordered_list_element: LeafNode(tag="li", value = unordered_list_element.replace('* ', '')).to_html(), splitted_block))
      unordered_list = f"<ul>{''.join(leaf_nodes)}</ul>"
      html_blocks.append(unordered_list)

    if type == 'ordered_list':
      ordered_list_elements = []
      splitted_block = block.split("\n")
      for index in range(len(splitted_block)):
        list_element = splitted_block[index].replace(f"{index+1}. ", "")
        node = LeafNode(tag="li", value = list_element).to_html()
        ordered_list_elements.append(node)
      ordered_list = f"<ol>{''.join(ordered_list_elements)}</ol>"
      html_blocks.append(ordered_list)

    if type == "quote":
      splitted_block = block.split("\n\n")
      replaced_block = block.replace(">", "")
      node = LeafNode(tag="blockquote", value = replaced_block).to_html()
      html_blocks.append(node)
    if type == "paragraph":
      splitted_block = block.split("\n\n")
      joined_block = "".join(splitted_block)
      node = LeafNode(tag="p", value = joined_block).to_html()
      html_blocks.append(node)

  join_all_nodes = "".join(html_blocks)
  final_node = f"<div>{join_all_nodes}</div>"
  return final_node


