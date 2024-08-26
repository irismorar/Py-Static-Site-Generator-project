def markdown_to_blocks(markdown):
  blocks = []
  splited_texts = markdown.split("\n\n")
  for text in splited_texts:
    if text == "":
      continue
    x = stripped_text(text)
    blocks.append(x.strip())
  return blocks

# original version
#def strip_whitespace(text):
#  new_array= []
#  splited_text = text.split("\n")
#  for item in splited_text:
#    x = item.strip()
#    new_array.append(x)
#  return "\n".join(new_array)

# succint version
def stripped_text(text):
  return "\n".join(map(lambda a: a.strip(),text.split("\n")))

