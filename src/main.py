import os
from textnode import TextNode, TextType

from static_pieces import*
from generation_funcs import *

    
static = ("./static")
public =  ("./public")
content = ("./content")
template = ("./template.html")

def main():
   
    print("Deleting public directory...")
    if os.path.exists(public):
        shutil.rmtree(public)

    print ("Copying static files to public directory...")    
    stat_to_pub_copy(static, public) 
    
    generate_page_recursively(content,
            template,
            public
            )


if __name__ == "__main__": 
    main()
