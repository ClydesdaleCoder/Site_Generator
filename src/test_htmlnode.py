import unittest

from htmlnode import HTMLNode,ParentNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self): 
        node = HTMLNode(None,None,None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertIsInstance(node.props_to_html(), str)
    def test_children(self):
        node= HTMLNode(None,None,['apple', 'banana', 'cherry'])
        self.assertIsInstance(node.children,list)
    
    def test_repr(self): 
        node= HTMLNode(None,None,['apple', 'banana', 'cherry'], {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertIsInstance(node.__repr__(), str)

    def test_empty_props(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        assert result == ""

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_props(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(),"Click me!") 

    def test_error(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            LeafNode("a", None).to_html() 

class TestParentNode(unittest.TestCase):    
    def test_Parent(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
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
