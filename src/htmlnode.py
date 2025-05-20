from textnode import *

class HTMLNode:
    def __init__(self,tag =None,value =None,children =None,props =None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []        
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses must implement this")
    def props_to_html(self):
        if isinstance(self.props, dict):
            pairs = "" 
            for key,value in self.props.items():
                pairs += f' {key}="{value}"'
            return pairs
        else: 
            return ""
    def __repr__(self): 
        return (f" tag : {self.tag}\n value: {self.value}\nchildren: {self.children}\nprops: {self.props}")

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

class ParentNode(HTMLNode):
    def __init__(self, tag , children, props = None): 
         super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: No Tag Present")
        elif self.children is None: 
            raise ValueError("Error: No Children Present")
        kid = ""
        for child in self.children: 
            kid = kid + child.to_html()
        return f"<{self.tag}>{kid}</{self.tag}>"

