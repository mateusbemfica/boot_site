import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_ne(self):
        node = HTMLNode("a", "blue", HTMLNode(), {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "blue", HTMLNode(), {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("a", "blue", HTMLNode(), {"href": "https://www.google.com"})
        answ = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), answ)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
   
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
    )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
if __name__ == "__main__":
    unittest.main()
