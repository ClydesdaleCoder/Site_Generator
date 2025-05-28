from textnode import *  
from  extractions import *

def split_nodes_image(old_nodes):
    split_nodes = []
    
    for  old in old_nodes: 
        processed = extract_markdown_images(old.text)

        if not processed:
            split_nodes.append(old)

        else:
            current_text = old.text
            for p in processed:
                image_section = "!["+ p[0] + "("+ p[1] + ")"
                
                around_image = current_text.split(image_section,1)
                
                if around_image[0] != "":
                    
                    split_nodes.append(TextNode(around_image[0],TextType.TEXT))

                split_nodes.append(TextNode(p[0],TextType.IMAGE,p[1]))

                remainder = around_image[1]
                
                current_text = remainder

            if current_text != "":
                split_nodes.append(TextNode(current_text,TextType.TEXT))

