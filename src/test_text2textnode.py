import unittest

from text2textnode import *

class Testtext2textnode(unittest.TestCase):

    def test_func(self): 
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        results = text_to_textnode(text)

        self.assertListEqual(
            [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                        ],
            results,
                )
    def test_links_both_ends(self): 
        text = "[linkA](www.google.com)**text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        results = text_to_textnode(text)

        self.assertListEqual(
                    [
                    TextNode("linkA", TextType.LINK,"www.google.com"),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                            ],
                results,

                )


    def test_bold_both_ends(self): 
        text = "**text A** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and bold **text B**"

        results = text_to_textnode(text)

        self.assertListEqual(
                    [
                    TextNode("text A", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and bold ", TextType.TEXT),
                    TextNode("text B", TextType.BOLD),
                            ],
                results,

                )



    def test_all_images(self): 
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![test image](https://boot.dev)"

        results = text_to_textnode(text)

        self.assertListEqual(
            [
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode("test image", TextType.IMAGE,"https://boot.dev"),
                        ],
                results,
                )


    def test_all_links(self): 
        text = "[obi wan link](https://i.imgur.com/fJRm4Vk.jpeg)[test link](https://boot.dev)"

        results = text_to_textnode(text)

        self.assertListEqual(
            [
                    TextNode("obi wan link", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode("test link", TextType.LINK,"https://boot.dev"),
                        ],
                results,
                )

    def test_none(self): 
        text = ""
        
        results = text_to_textnode(text)
          

        self.assertListEqual(
            [],results,)





if __name__ == "__main__":
    unittest.main()
