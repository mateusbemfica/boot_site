import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_ne(self):
        node = HTMLNode("a", "blue", HTMLNode(), {"href": "https://www.google.com"})
        node2 = HTMLNode("a", "blue", HTMLNode(), {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("a", "blue", HTMLNode(), {"href": "https://www.google.com"})
        answ = "href=https://www.google.com"
        self.assertEqual(node.props_to_html(), answ)

if __name__ == "__main__":
    unittest.main()
