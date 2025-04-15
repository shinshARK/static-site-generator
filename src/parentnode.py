from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
                raise ValueError("invalid HTML: no children")
        
        children = ''
        for child in self.children:    
            children = children + child.to_html()
            
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={repr(self.tag)}, children={repr(self.children)}, props={repr(self.props)})"
    

