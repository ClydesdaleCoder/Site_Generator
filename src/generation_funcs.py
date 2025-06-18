import os

from block_markdown import *
from extractions import *
from pathlib import Path

def generate_page_recursively(dir_path_content,template_path, dest_dir_path): 
    #crawl through directories
    for dirpath,dirnames,filenames in os.walk(dir_path_content): 
        for filename in filenames: #handles the files
            #create new destination file
            new_dest  = os.path.join(dest_dir_path,(Path(dirpath).relative_to(dir_path_content)))
            new_dest_file = os.path.join(new_dest , filename)
            final_dest_file = new_dest_file.replace(".md" , '.html') 

            #create new source file path
            new_source_file = os.path.join (dirpath , filename)
            
            #call the generation
            generate_page(new_source_file, template_path , final_dest_file)

def generate_page(from_path, template_path, dest_path):
    print (f'Generating page from {from_path} to {dest_path} using {template_path}')
    
    from_file = open(from_path, "r")
    markdown_content  = from_file.read()
    from_file.close()
        
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    from_html = node.to_html()

    from_title =extract_title(markdown_content)

    final_page = template.replace("{{ Title }}",from_title).replace("{{ Content }}", from_html)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok =True)
    to_file = open(dest_path , "w" )
    to_file.write(final_page)
        

