from textnode import TextNode, TextType


def main() -> None:
    print("Hello World")
    node = TextNode("Hello World", TextType.BOLD, "www.duck.pt")
    print(node)


if __name__ == "__main__":
    main()
