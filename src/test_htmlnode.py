import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="link", props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(str(node.props), str(node2.props))


    
    def test_props_top_html(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_constructor_default_none(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

if __name__ == "__main__":
    unittest.main()