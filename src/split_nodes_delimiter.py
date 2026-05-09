from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter is None or not isinstance(delimiter, str):
                raise Exception("No delimiter")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
 
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("unmatched delimiter")
        for idx, value in enumerate(parts):
            if value == "":
                continue
            actual_type = TextType.TEXT if idx % 2 == 0 else text_type
            new_nodes.append(TextNode(value, actual_type))
    return new_nodes

            