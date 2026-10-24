from textnode import TextNode, TextType


def main():
    text_node = TextNode("This is a TextNode", TextType.LINK, "www.duck.com")
    print(text_node)


main()
