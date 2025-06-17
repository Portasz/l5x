'''
Module defining the Rung class which stores the logic and comments for a rung in a program.



'''

class Rung:
    def __init__(self, element, lang):
        self.element = element
        self.lang = lang

        text_element = self.element.find("Text")
        self.text_cdata_element = text_element.find("CDATAContent") if text_element is not None else None

        comment_element = self.element.find("Comment")
        comment_cdata_element = comment_element.find("CDATAContent") if comment_element is not None else None


        #self.text = self.text_cdata_element.text if self.text_cdata_element is not None else ""
        self.comment = comment_cdata_element.text if comment_cdata_element is not None else ""

        '''
        Could technically use this to get the text or comment, but we're currently using the above code
        so that it's cleaner when the text or comment is not present. Also allows access to the elements
        directly if needed.
        self.text = self.element.find("Text").find("CDATAContent").text.strip() if self.element.find("Text") is not None else ""
    '''
        
    @property
    def text(self):
        return self.element.find("Text").find("CDATAContent").text
        #return self.text

    def func(self, value):
        self.element.find("Text").find("CDATAContent").text = value

    @text.setter
    def text(self, value):
        """Set the rung text."""
        if not isinstance(value, str):
            raise TypeError("Text must be a string.")
        
        print(f"Setting text to: {value}")
        text_element = self.element.find("Text")
        print(f"Text element: {text_element}")
        
        if text_element is not None:
            cdata_element = text_element.find("CDATAContent")
            print(f"CDATA element: {cdata_element}")
            
            if cdata_element is not None:
                cdata_element.text = value
                print(f"Successfully set text to: {cdata_element.text}")
            else:
                print("CDATAContent element is None!")
        else:
            print("Text element is None!")




'''    @text.setter
    def text(self, value):
        """Set the rung text."""
        if not isinstance(value, str):
            raise TypeError("Text must be a string.")
        
        text_element = self.element.find("Text")
        if text_element is None:
            raise ValueError("Text element not found in rung")
        
        cdata_element = text_element.find("CDATAContent")
        if cdata_element is None:
            raise ValueError("CDATAContent element not found in Text element")
        
        cdata_element.text = value'''
