class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NoteImplementedError

    def props_to_html(self):
        props_html = ""
        if self.props is None:
            return ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
   
    def to_html(self):
        if self.value == None:
            raise  ValueError("invalid")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
 
    def __repr__(self):
        f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        x = ""
        if self.tag is None:
            raise ValueError ("invalid")
        if self.children is None:
            raise ValueError ("invalid children")
        for c in self.children:
           x += c.to_html()
        return f"<{self.tag}>{x}</{self.tag}>"
