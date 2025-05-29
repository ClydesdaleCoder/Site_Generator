import unittest

from split_images_link import *

class Testsplit_nodes_image(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_no_images(self):
        node = TextNode(
            "This is text with no image", 
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no image", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_beginning_image(self): 
        node = TextNode(
                "![image](www.google.com) the image came first",
                TextType.TEXT,
                )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("image",TextType.IMAGE, "www.google.com"),
                    TextNode(" the image came first", TextType.TEXT)
                    ],
                new_nodes,
                )

class Testsplit_nodes_link(unittest.TestCase):
    def test_split_link(self):
        node = TextNode(
            "This is text with an [link A](https://i.imgur.com/zjjcJKZ.png) and another [link B](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link A", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link B", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    
    def test_no_link(self):
        node = TextNode(
            "This is text with no link" ,
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no link", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_beginning_link(self): 
        node = TextNode(
                "[link](www.google.com) the link came first",
                TextType.TEXT,
                )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
                [
                    TextNode("link",TextType.LINK, "www.google.com"),
                    TextNode(" the link came first", TextType.TEXT)
                    ],
                new_nodes,
                )


if __name__ == "__main__":
    unittest.main()       
