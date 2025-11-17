import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_tag(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_single_prop(self):
        node = HTMLNode(
            tag="img",
            props={"src": "/images/my_image.png"}
        )
        expected_output = ' src="/images/my_image.png"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(
            tag="p",
            props={}
        )
        expected_output = ""
        self.assertEqual(node.props_to_html(), expected_output)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_anchor_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        expected_html = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_heading(self):
        node = LeafNode("h1", "The Main Title")
        self.assertEqual(node.to_html(), "<h1>The Main Title</h1>")

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")


class TestParentNode(unittest.TestCase):

    def test_to_html_simple_children(self):

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        expected = "<div><span><b>grandchild</b></span></div>"
        self.assertEqual(parent_node.to_html(), expected)

    def test_to_html_with_props(self):
        child_node = LeafNode("a", "Click Here", {"href": "https://example.com"})
        parent_node = ParentNode("div", [child_node], {"id": "main", "class": "container"})
        html1 = '<div id="main" class="container"><a href="https://example.com">Click Here</a></div>'
        html2 = '<div class="container" id="main"><a href="https://example.com">Click Here</a></div>'

        result = parent_node.to_html()
        self.assertTrue(result == html1 or result == html2)

if __name__ == "__main__":
    unittest.main()