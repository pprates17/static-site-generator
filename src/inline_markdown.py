from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown syntax: formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                result_list.append(TextNode(sections[i], TextType.TEXT))
            else:
                result_list.append(TextNode(sections[i], text_type))
    return result_list
