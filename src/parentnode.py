from libxml2mod import children

from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None or tag == "":
            raise ValueError("ParentNode requires a tag.")
        if children is None or len(children) == 0:
            raise ValueError("ParentNode requires a list of child nodes.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("Parent nodes must have tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent nodes must have children")
        props = self.props_to_html()
        html_kids = ""
        for child in self.children:
            html_kids += child.to_html()
        return f"<{self.tag}{props}>{html_kids}</{self.tag}>"