
'''
Module to implement the Program class, which represents a single program within an L5X project.

'''
from .tag import Scope
from .dom import ElementDict
from l5x.rung import Rung
from .ladder import Ladder
        


#placehold for the Routine class, which should be defined in a separate module
class Routine:
     def __init__(self, element, lang):
        self.element = element
        self.lang = lang

        #currently, the only supported logic element is ladder logic, so RLLContent.
        #this can be expanded in the future to support other logic types
        self.rll_content_element = element.find("RLLContent")
        logic_list = self.rll_content_element.findall("Rung")
        if logic_list is None:
            logic_list = []
        rung_list = [Rung(rung_element, lang) for rung_element in logic_list]
        self.ladder = Ladder(element=self.rll_content_element, rungs=rung_list)

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

        
        

    
    
