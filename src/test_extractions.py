import unittest

from extractions import *

class Testextractions(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
         )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches= extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),("to youtube","https://www.youtube.com/@bootdotdev")], matches)


    def test_extract_markdown_blank_images(self):
        matches = extract_markdown_images(
            "This is text with  nothing!"
         )
        self.assertListEqual([],matches)


    def test_extract_markdown_no_links(self):
        matches = extract_markdown_links(
            "This is text with  nothing!"
         )
        self.assertListEqual([],matches)


    def test_extract_title_function(self):
        Hello = extract_title("# Hello")
        self.assertEqual("Hello",Hello)

    def test_extract_title_with_lines(self):
        Hello = extract_title("# Hello\nHere's the deal, **I like Tolkien**.")
        self.assertEqual("Hello\nHere's the deal, **I like Tolkien**.",Hello)

    def test_extraction_exception(self):
        Hello = "Hello\nHere's the deal, **I like Tolkien**."
        self.assertRaises(Exception,extract_title, Hello)


if __name__ == "__main_":
    unittest.main()   
