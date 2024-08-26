class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
  
  def props_to_html(self):
    if not self.props:
      return ''
    result = []
    for key, value in self.props.items():
        result.append(f"{key}='{value}'")
    return ' '.join(result)
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props={}):
    super().__init__(tag, value, children=None, props=props)
  
  def to_html(self):
    if not self.value:
      raise ValueError("You must enter a value")
    if not self.tag:
      return self.value
    else:
      result = ''
      for key, value in self.props.items():
        result += f"{key}='{value}' "
      result = result.strip()
      self.props = result
      if result:
        return f"<{self.tag} {self.props}>{self.value}</{self.tag}>"
      else:
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
  def __init__(self, tag, children):
    super().__init__(tag, value=None, children=children, props=None)

  def to_html(self):
    if not self.tag:
      raise ValueError("You must enter a tag")
    if not self.children:
      raise ValueError("You must enter at least one child")
    else:
      result = ''
      for child in self.children:
        result += child.to_html()
      return f"<{self.tag}>{result}</{self.tag}>"
