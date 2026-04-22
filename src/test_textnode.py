import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type.value, node2.text_type.value)
        self.assertEqual(node.url, node2.url)
    
    def test_text_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node, but another one", TextType.BOLD)
        self.assertNotEqual(node.text, node2.text)
        self.assertEqual(node.text_type.value, node2.text_type.value)
        self.assertEqual(node.url, node2.url)
    
    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        node2 = TextNode("This is a text node, but another one", TextType.ITALIC, "https://www.example.com")
        self.assertNotEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type.value, node2.text_type.value)
        self.assertEqual(node.url, node2.url)
    
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a TEXT NODE", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
