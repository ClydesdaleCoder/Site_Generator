import unittest

from splitnodedelimiter import  *

class Testsplit_nodes_delimiter(unittest.TestCase):

    def test_bold(self): 
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result,[
            TextNode("This is ",TextType.TEXT),
            TextNode("bold",TextType.BOLD),
            TextNode(" text",TextType.TEXT)
            ]
        )

    def test_bold(self): 
        node = TextNode("Here is `code` and another `code block` sir.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result,[
            TextNode("Here is ",TextType.TEXT),
            TextNode("code",TextType.CODE),
            TextNode(" and another ",TextType.TEXT),
            TextNode("code block",TextType.CODE),
            TextNode(" sir.",TextType.TEXT)
            ]
        )
    def test_missing_delimiter(self):
        node = TextNode("This will **fail", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiples(self): 
        nodes = [TextNode("Here is `code` and another `code block` sir.", TextType.TEXT),TextNode("Here is `more code` and another `code block` maam.", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("Here is ",TextType.TEXT),
            TextNode("code",TextType.CODE),
            TextNode(" and another ",TextType.TEXT),
            TextNode("code block",TextType.CODE),
            TextNode(" sir.",TextType.TEXT),
            TextNode("Here is ",TextType.TEXT),
            TextNode("more code",TextType.CODE),
            TextNode(" and another ",TextType.TEXT),
            TextNode("code block",TextType.CODE),
            TextNode(" maam.",TextType.TEXT)
            ]
        self.assertEqual(len(result),len(expected))
        for i in range(len(result)):
            self.assertEqual(result[i].text, expected[i].text)
            self.assertEqual(result[i].text_type, expected[i].text_type)

if __name__ == "__main__":
    unittest.main()
