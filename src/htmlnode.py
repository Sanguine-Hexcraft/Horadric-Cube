class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # a string representing the HTML tag name (e.g. "p", "a", "h1", etc)
        self.tag = tag
        # a string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.value = value
        # a list of HTMLNode objects representing the children of this node
        self.children = children
        # a dictionary of key-value pairs representing the attributes of the HTML tag.
        # for example, a link (<a> tag) might have {"href": "https://www.google.com"}
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ""
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
            
        return props_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
