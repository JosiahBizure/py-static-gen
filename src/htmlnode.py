class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError() # Child classes to override this method to render themselves as HTML
    
    def props_to_html(self):
        html_attributes = ""
        for key in self.props:
            html_attributes += f" {key}=\"{self.props[key]}\""
        
        return html_attributes
    
    def __repr__(self):
        return (f"tag: {self.tag}\n"
                f"value: {self.value}\n"
                f"children: {self.children}\n"
                f"props: {self.props}")