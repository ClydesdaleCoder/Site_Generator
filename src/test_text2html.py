import unittest

from text2html import *

class TestText2Html(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_value_error(self):
        node = TextNode("d","If you see this something is wrong")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
    
    def test_image(self):
        node = TextNode("image here",TextType.IMAGE,"www.image.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.props,{"src":"www.image.org", "alt": "image here"})

    def test_image(self):
        node = TextNode("link here",TextType.LINK,"www.image.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"link here")
        self.assertEqual(html_node.props,{"href":"www.image.org"})

if __name__ == "__main__":
     unittest.main()
