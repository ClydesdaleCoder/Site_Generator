from textnode import TextNode, TextType

from static_pieces import*

def main():
    static = pathlib.Path("~/home/elguero/workspace/github/clydesdalecoder/Site_Generator/static")
    public =  pathlib.Path("~/home/elguero/workspace/github/clydesdalecoder/Site_Generator/public")
    stat_to_pub_copy(static, public) 

if __name__ == "__main__": 
    main()
