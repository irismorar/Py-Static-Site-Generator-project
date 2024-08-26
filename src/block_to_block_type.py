def block_to_block_type(markdown_text_block):
  splitted_by_space = markdown_text_block.split(' ')
  splitted_by_enter = markdown_text_block.split("\n")
  length_by_enter = len(splitted_by_enter)

  for i in range(7):
    if splitted_by_space[0] == "#"*i:
      return "heading"

  if markdown_text_block[:3] == "```" and  markdown_text_block[-3:] == "```":
    return "code"

  if markdown_text_block[0] == ">":
    return "quote"

  if markdown_text_block[:2] == "* " or markdown_text_block[:2] == "- ":
    return "unordered_list"

  for i in range(length_by_enter):
     if splitted_by_enter[i].split(" ")[0] == f"{i+1}.":
      return "ordered_list"

  return "paragraph"