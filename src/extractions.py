import re

def extract_markdown_images(text): 
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def extract_title(markdown):
    if markdown.startswith("#"):
        return markdown.strip(" # ")

    if not markdown.startswith("#"):
        raise Exception("Missing h1 Header")
