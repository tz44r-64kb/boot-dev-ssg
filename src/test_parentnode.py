import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestLeafNode(unittest.TestCase):
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

    def text_to_html_with_multiple_children(self):
        first_child_node = LeafNode("span", "first_child")
        second_child_node = LeafNode("span", "second_child")
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>first_child</span><span>second_child</span></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("a", [child_node], props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(parent_node.to_html(), '<a href="https://www.google.com" target="_blank"><span>child</span></a>')

    def test_to_html_no_tag(self):
        node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()