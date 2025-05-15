from textnode import TextNode, TextType

def main():
    test = TextNode("dummy text",TextType.LINK,"www.google.com")

    print(test)

if __name__ == "__main__": 
    main()
