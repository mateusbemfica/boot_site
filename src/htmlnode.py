class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NoteImplementedError

    def props_to_html(self):
        for i,j in self.props.items():
            return f"{i}={j}"

    def __repr__(self):
        f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 
