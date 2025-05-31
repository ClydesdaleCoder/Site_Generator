
def markdown_to_blocks(markdown):
    if markdown == "":
        raise Exception("Please Provide Text")
    split_lines = markdown.split("\n\n")
    stripped_lines = []
    for s in split_lines:
        current_line = s.strip()
        stripped_lines.append(current_line)
    return stripped_lines
