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

if __name__ == "__main_":
    unittest.main()   
