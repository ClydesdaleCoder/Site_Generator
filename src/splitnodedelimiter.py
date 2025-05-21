from textnode import *

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for old in old_nodes: 
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue
        text = old.text
        
        while delimiter in text:
            start_index = text.find(delimiter)
             
            if start_index != -1: 
                end_index = text.find(delimiter, start_index + len(delimiter))

                if end_index == -1:
                    raise ValueError(f"Invalid markdown: missing closing delimiter '{delimiter}'")
                
                before_text = text[:start_index]
                
                between_text= text[start_index + len(delimiter):end_index]

                after_text = text[end_index + len(delimiter):]
                
                if before_text:
                    new_nodes.append(TextNode(before_text,TextType.TEXT))
                
                if between_text: 
                    new_nodes.append(TextNode(between_text,text_type))
                
                text = after_text
            else:
                break

        if text:   
            new_nodes.append(TextNode(text,TextType.TEXT))

    return new_nodes

    
    
