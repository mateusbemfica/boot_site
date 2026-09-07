from enum import Enum
from htmlnode import *
from extr import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC  = "italic"
    CODE  = "code"
    LINK  = "link"
    IMAGE = "image"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    def __repr__(self):
        TEXT = self.text
        TEXT_TYPE = self.text_type.value
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": {text_node.text}})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src":{text_node.url}, "alt":{text_node.text}})
        case _:
            raise Exception("non type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    y = []
    if old_nodes.text_type != TextType.TEXT:
        y.extend(old_nodes)
    if delimiter not in TextType(Enum):
        raise ValueError("invalid")
    x = old_nodes.split("delimiter")
    for i in x:
        if i[0] == delimiter:
            y.append(TextNode(i, text_type))
        y.append(TextNode(i, TextType.TEXT))
    return y

def split_nodes_image(old_nodes):
    y = []
    i = 0
    x = Extr.extract_markdown_images(old_nodes[i].text)
    for j in Extr.extract_markdown_images(old_nodes[i].text):



def split_nodes_link(old_nodes):
    y = []
    x = Extr.extract_markdown_links(old_nodes[0].text)
    for i in x:
        if i in x:
            y.append(TextNode(i[0], TextType.LINK, i[1]))
        y.append(TextNode(i, TextType.TEXT))
    return y
