import unittest
from leafnode import LeafNode 

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

if __name__ == "__main__":
     unittest.main()
