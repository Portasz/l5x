from .rung import Rung
import xml.etree.ElementTree as ElementTree
from .dom import CDATA_TAG

class RungFactory:
    """Factory for creating properly configured Rung objects."""

    @staticmethod
    def create_rung(rung_type='N', text=None, comment=None, number=0):
        element = RungFactory._create_base_xml(rung_type=rung_type)
        rung = Rung(element)
        rung.type = rung_type
        rung.number = number
        if text is not None:
            rung.text = text
        if comment is not None:
            rung.comment = comment
        return rung
    
    @staticmethod
    def _create_base_xml(rung_type='N'):
        """Internal helper for XML creation."""
        xml_elem = ElementTree.Element('Rung')
        xml_elem.set('Type', rung_type)
        xml_elem.set('Number', '0')  # Will be renumbered later
        
        # Required subelements
        comment_elem = ElementTree.SubElement(xml_elem, 'Comment')
        text_elem = ElementTree.SubElement(xml_elem, 'Text')

        ElementTree.SubElement(comment_elem, CDATA_TAG)
        ElementTree.SubElement(text_elem, CDATA_TAG)
        
        return xml_elem