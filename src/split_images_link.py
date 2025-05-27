from textnode import *  
from  extractions import *

def split_nodes_image(old_nodes):
    split_nodes = []
    
    for  old in old_nodes: 
        processed = extract_markdown_images(old.text)

        if not processed:
            split_nodes.append(old)

        else:
        
        
