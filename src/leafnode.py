from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str = None,
            value: str = None,
            props: dict | None = None
            ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf node must have a value")
        if self.tag is None:
            return f"{self.value}"
        html_str = ""
        html_str += f"<{self.tag}"
        if self.props is not None:
            for prop in self.props:
                html_str += f" {prop}={self.children[prop]}"
        html_str += f">{self.value}</{self.tag}>"
        print(f"HTML: {html_str}")
        return html_str

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
