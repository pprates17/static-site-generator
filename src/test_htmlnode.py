import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "div",
            "This is a div",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "This is a div",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "This is a HTML Node",
            None,
            {"class": "hello", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="hello" href="https://boot.dev"',
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, This is a paragraph, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "I am a link!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">I am a link!</a>',
        )

    def test_leaf_repr(self):
        node = LeafNode("b", "Bold Text!")
        self.assertEqual(node.__repr__(), "LeafNode(b, Bold Text!, None)")


if __name__ == "__main__":
    unittest.main()
