from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        if self.value is None:
            raise ValueError("All Leaf Nodes must have a value.")

    def to_html(self):
        if self.tag is None:
            return self.value
        attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"