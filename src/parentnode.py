from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError(f"no tag")
        if self.children is None:
            raise ValueError(f"no children")
        result = ""
        for node in self.children:
            result += node.to_html()
        return f"<{self.tag}{self.props_to_html() if self.props else ''}>{result}</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"   