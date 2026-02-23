from textnode import TextNode, TextType

def main():
    new_textnode = TextNode("This is some anchor text", TextType.LINK, "http://www.boot.dev")
    print(new_textnode)


main()
