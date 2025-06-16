
'''
Module to implement the Program class, which represents a single program within an L5X project.

'''
from .tag import Scope
from .dom import ElementDict

class Rung:
    def __init__(self, element, lang):
        self.element = element
        self.lang = lang

        text_element = self.element.find("Text")
        text_cdata_element = text_element.find("CDATAContent") if text_element is not None else None

        comment_element = self.element.find("Comment")
        comment_cdata_element = comment_element.find("CDATAContent") if comment_element is not None else None


        self.text = text_cdata_element.text.strip() if text_cdata_element is not None else ""
        self.comment = comment_cdata_element.text.strip() if comment_cdata_element is not None else ""

        '''
        Could technically use this to get the text or comment, but we're currently using the above code
        so that it's cleaner when the text or comment is not present. Also allows access the elements
        directly if needed.
        self.text = self.element.find("Text").find("CDATAContent").text.strip() if self.element.find("Text") is not None else ""
    '''
        


#placehold for the Routine class, which should be defined in a separate module
class Routine:
     def __init__(self, element, lang):
        self.element = element
        self.lang = lang

        #currently, the only supported logic element is ladder logic, so RLLContent.
        #this will be expanded in the future to support other logic types
        logic_list = element.find("RLLContent").findall("Rung")
        self.rungs = [Rung(rung_element, lang) for rung_element in logic_list]


class Program(Scope):
    def __init__(self, element, lang):
        #attributes that have to do with XML
        self.lang = lang
        self.element = element

        #attributes that involve the PLC data
        routines_element = element.find('Routines')
        self.routines = ElementDict(parent=routines_element,
                                    key_attr='Name',
                                    value_type=Routine,
                                    value_args=[lang])

        super().__init__(element, lang)

        
        

    
    