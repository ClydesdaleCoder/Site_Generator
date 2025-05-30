from split_images_link import *  

from splitnodedelimiter import *

from textnode import *

def text_to_textnode(text): 
    text_nodes = []
    working_text = [TextNode(f"{text}",TextType.TEXT)] 
    functions = [split_nodes_image, split_nodes_link , split_nodes_delimiter]
    current_text = working_text
    for func in functions: 
        delimiters = [('**',TextType.BOLD),('_',TextType.ITALIC),('`', TextType.CODE)]
        if func == split_nodes_delimiter :
            for d in delimiters: 
                result = split_nodes_delimiter(current_text,d[0],d[1])
                current_text = result
        else:
            result = func(current_text)
            current_text = result

    return current_text
