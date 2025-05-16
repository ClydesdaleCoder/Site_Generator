import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
