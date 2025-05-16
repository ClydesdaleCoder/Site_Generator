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

