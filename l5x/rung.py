import xml.etree.ElementTree as ElementTree
from dom import CDATA_TAG

'''
Module defining the Rung class which stores the logic and comments for a rung in a program.

'''

class Rung:
    def __init__(self, element, lang=None):
        self.lang = lang
        if element is None:
            #Number and Type attributes must be set elsewhere   
            dict = {"Number": "",
                    "Type": ""
                    }
            self.element=ElementTree.Element("Rung", attrib=dict)
        else:
            self.element=element

    @property
    def type(self):
        return self.element.attrib["Type"]

    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be a string.")
        self.element.attrib["Type"] = value  
    
    @property
    def number(self):
        return self.element.attrib["Number"]
    
    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("Number must be an integer")
        
        self.element.attrib["Number"] = str(value)

    @property
    def text(self):
        text = self._get_cdata_text("Text")
        return text

    @text.setter
    def text(self, value):
        """Set the rung text."""
        self._set_cdata_text("Text", value)

    @property
    def comment(self):
        comment = self._get_cdata_text("Comment")
        return comment

    @comment.setter
    def comment(self, value):
        """Set the rung comment."""
        self._set_cdata_text("Comment", value)


    def _set_cdata_text(self, parent_tag: str, value: str):
        if not isinstance(value, str):
            raise TypeError("Value must be a string.")

        # Find or create the parent element
        element = self.element.find(parent_tag)
        if element is None:
            element = ElementTree.SubElement(self.element, parent_tag)

        # Find or create the CDATAContent child
        cdata_element = element.find(CDATA_TAG)
        if cdata_element is None:
            cdata_element = ElementTree.SubElement(element, CDATA_TAG)

        # Set the text
        cdata_element.text = value

    def _get_cdata_text(self, parent_tag: str):
        # Ensure self.element is not None
        if self.element is None:
            return None

        element = self.element.find(parent_tag)
        if element is None:
            return None

        cdata_elem = element.find(CDATA_TAG)
        if cdata_elem is None:
            return None

        return cdata_elem.text
            
                


