import re

def extract_markdown_images(text): 
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception("Missing h1 Header")
    
    if markdown.startswith("#"):
        no_header = markdown.strip(" # ")
        title_sep = no_header.split("\n",1)
        return title_sep[0]

