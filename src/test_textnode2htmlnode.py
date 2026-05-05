from textnode import TextNode, TextType
from textnode2htmlnode import text_node_to_html_node
import unittest

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_anchor(self):
        node = TextNode("This is an anchor node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com" target="_blank">This is an anchor node</a>')

    def test_img(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.img.example")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.img.example" alt="This is an image node"></img>')

    def test_not_a_text_node(self):
        node = TextNode("fake", "INVALID")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        
        self.assertEqual(str(context.exception), "Not a text node")


