import os
import sys
from textnode import TextNode, TextType

from static_pieces import*
from generation_funcs import *

    
static = ("./static")
content = ("./content")
template = ("./template.html")
default_basepath = "/"
docs = ("./docs")

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting docs directory...")
    if os.path.exists(docs):
        shutil.rmtree(docs)

    print ("Copying static files to docs directory...")    
    stat_to_pub_copy(static, docs) 
    
    generate_page_recursively(content,
            template,
            docs,
            basepath
            )


if __name__ == "__main__": 
    main()
