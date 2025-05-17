from htmlnode import HTMLNode

class LeafNode(HTMLNode): 
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,[],props)
        

    def to_html(self): 
        if self.value is None: 
            raise ValueError("Leaf Node must have a Value")
        
        elif self.tag is None: 
            return self.value
        else:
            props_str= ""
            
            if self.props:
                props_str = self.props_to_html()
            
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

