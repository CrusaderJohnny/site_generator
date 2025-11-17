from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if self.text_type == other.text_type:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type.value:
        case "text":
            textNode = LeafNode(tag=None, value=text_node.text)
            return textNode
        case "bold":
            boldNode = LeafNode(tag="b", value=text_node.text)
            return boldNode
        case "italic":
            italicNode = LeafNode(tag="i", value=text_node.text)
            return italicNode
        case "code":
            codeNode = LeafNode(tag="code", value=text_node.text)
            return codeNode
        case "link":
            linkNode = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
            return linkNode
        case "image":
            imageNode = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
            return imageNode
        case _:
            raise Exception(f"{text_node.text_type} is not a valid text type")