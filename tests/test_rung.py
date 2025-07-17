"""
Unit tests for a project's program's routine's rung objects.   :)
"""

from tests import fixture
import unittest
from l5x.rung import Rung
from l5x.dom import CDATA_TAG
import xml.etree.ElementTree as ElementTree

class TestRung(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a sample XML element for testing
        self.sample_xml = """
        <Rung Type="N" Number="1">
            <Comment>
                <![CDATA[Hello, World!]]>
            </Comment>
            <Text>
                <![CDATA[XIC(tag1)OTE(tag2);]]>
            </Text>
        </Rung>"""
        
        self.element = fixture.parse_xml(self.sample_xml)
        self.rung = Rung(self.element)

    def test_init_with_element(self):
        """Test initialization with an existing XML element."""
        rung = Rung(self.element)
        self.assertEqual(rung.element, self.element)
        self.assertIsNone(rung.lang)

    def test_init_with_element_and_lang(self):
        """Test initialization with element and language parameter."""
        rung = Rung(self.element, lang="en")
        self.assertEqual(rung.element, self.element)
        self.assertEqual(rung.lang, "en")

    def test_init_with_none_element(self):
        """Test initialization with None element creates new element."""
        rung = Rung(None)
        self.assertIsNotNone(rung.element)
        self.assertEqual(rung.element.tag, "Rung")
        self.assertEqual(rung.element.attrib["Number"], "")
        self.assertEqual(rung.element.attrib["Type"], "")

    def test_init_with_none_element_and_lang(self):
        """Test initialization with None element and language parameter."""
        rung = Rung(None, lang="es")
        self.assertIsNotNone(rung.element)
        self.assertEqual(rung.lang, "es")

    def test_type_property_getter(self):
        """Test type property getter."""
        self.assertEqual(self.rung.type, "N")

    def test_type_property_setter_valid_string(self):
        """Test type property setter with valid string."""
        self.rung.type = "G"
        self.assertEqual(self.rung.type, "G")
        self.assertEqual(self.rung.element.attrib["Type"], "G")

    def test_type_property_setter_invalid_type(self):
        """Test type property setter with invalid type raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.rung.type = 123
        self.assertEqual(str(context.exception), "Type must be a string.")

    def test_type_property_setter_none(self):
        """Test type property setter with None raises TypeError."""
        with self.assertRaises(TypeError):
            self.rung.type = None

    def test_number_property_getter(self):
        """Test number property getter."""
        self.assertEqual(self.rung.number, "1")

    def test_number_property_setter_valid_integer(self):
        """Test number property setter with valid integer."""
        self.rung.number = 42
        self.assertEqual(self.rung.number, "42")
        self.assertEqual(self.rung.element.attrib["Number"], "42")

    def test_number_property_setter_invalid_type(self):
        """Test number property setter with invalid type raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.rung.number = "invalid"
        self.assertEqual(str(context.exception), "Number must be an integer")

    def test_number_property_setter_float(self):
        """Test number property setter with float raises TypeError."""
        with self.assertRaises(TypeError):
            self.rung.number = 3.14

    def test_number_property_setter_none(self):
        """Test number property setter with None raises TypeError."""
        with self.assertRaises(TypeError):
            self.rung.number = None

    def test_text_property_getter(self):
        """Test text property getter."""
        expected_text = "XIC(tag1)OTE(tag2);"
        self.assertEqual(self.rung.text, expected_text)

    def test_text_property_setter_valid_string(self):
        """Test text property setter with valid string."""
        new_text = "XIC(tag3)OTE(tag4);"
        self.rung.text = new_text
        self.assertEqual(self.rung.text, new_text)

    def test_text_property_setter_empty_string(self):
        """Test text property setter with empty string."""
        self.rung.text = ""
        self.assertEqual(self.rung.text, "")

    def test_comment_property_getter(self):
        """Test comment property getter."""
        expected_comment = "Hello, World!"
        self.assertEqual(self.rung.comment, expected_comment)

    def test_comment_property_setter_valid_string(self):
        """Test comment property setter with valid string."""
        new_comment = "This is a test comment"
        self.rung.comment = new_comment
        self.assertEqual(self.rung.comment, new_comment)

    def test_comment_property_setter_empty_string(self):
        """Test comment property setter with empty string."""
        self.rung.comment = ""
        self.assertEqual(self.rung.comment, "")

    def test_set_cdata_text_invalid_type(self):
        """Test _set_cdata_text with invalid type raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.rung._set_cdata_text("Text", 123)
        self.assertEqual(str(context.exception), "Value must be a string.")

    def test_set_cdata_text_none_value(self):
        """Test _set_cdata_text with None value raises TypeError."""
        with self.assertRaises(TypeError):
            self.rung._set_cdata_text("Text", None)

    def test_set_cdata_text_creates_new_parent_element(self):
        """Test _set_cdata_text creates new parent element if it doesn't exist."""
        # Create a fresh rung without Text element
        fresh_rung = Rung(None)
        fresh_rung._set_cdata_text("Text", "New text")
        
        # Verify the element structure was created
        text_element = fresh_rung.element.find("Text")
        self.assertIsNotNone(text_element)
        cdata_element = text_element.find(CDATA_TAG)
        self.assertIsNotNone(cdata_element)
        self.assertEqual(cdata_element.text, "New text")

    def test_set_cdata_text_creates_new_cdata_element(self):
        """Test _set_cdata_text creates new CDATA element if it doesn't exist."""
        # Create a parent element without CDATA child
        text_element = ElementTree.SubElement(self.rung.element, "NewText")
        
        self.rung._set_cdata_text("NewText", "Test content")
        
        cdata_element = text_element.find(CDATA_TAG)
        self.assertIsNotNone(cdata_element)
        self.assertEqual(cdata_element.text, "Test content")

    def test_get_cdata_text_element_none(self):
        """Test _get_cdata_text with None element."""
        rung = Rung(None)
        rung.element = None
        result = rung._get_cdata_text("Text")
        self.assertIsNone(result)

    def test_get_cdata_text_parent_not_found(self):
        """Test _get_cdata_text when parent element is not found."""
        result = self.rung._get_cdata_text("NonExistentTag")
        self.assertIsNone(result)

    def test_get_cdata_text_cdata_element_not_found(self):
        """Test _get_cdata_text when CDATA element is not found."""
        # Create a parent element without CDATA child
        ElementTree.SubElement(self.rung.element, "EmptyTag")
        
        result = self.rung._get_cdata_text("EmptyTag")
        self.assertIsNone(result)

    def test_get_cdata_text_cdata_element_no_text(self):
        """Test _get_cdata_text when CDATA element has no text."""
        # Create structure with empty CDATA element
        parent = ElementTree.SubElement(self.rung.element, "EmptyText")
        cdata_elem = ElementTree.SubElement(parent, CDATA_TAG)
        cdata_elem.text = None
        
        result = self.rung._get_cdata_text("EmptyText")
        self.assertIsNone(result)

    def test_text_property_with_missing_elements(self):
        """Test text property when Text element doesn't exist."""
        fresh_rung = Rung(None)
        self.assertIsNone(fresh_rung.text)

    def test_comment_property_with_missing_elements(self):
        """Test comment property when Comment element doesn't exist."""
        fresh_rung = Rung(None)
        self.assertIsNone(fresh_rung.comment)

    def test_text_setter_creates_complete_structure(self):
        """Test that text setter creates complete XML structure."""
        fresh_rung = Rung(None)
        test_text = "XIC(newTag)OTE(output);"
        fresh_rung.text = test_text
        
        # Verify complete structure
        self.assertEqual(fresh_rung.text, test_text)
        text_element = fresh_rung.element.find("Text")
        self.assertIsNotNone(text_element)
        cdata_element = text_element.find(CDATA_TAG)
        self.assertIsNotNone(cdata_element)
        self.assertEqual(cdata_element.text, test_text)

    def test_comment_setter_creates_complete_structure(self):
        """Test that comment setter creates complete XML structure."""
        fresh_rung = Rung(None)
        test_comment = "This is a new comment"
        fresh_rung.comment = test_comment
        
        # Verify complete structure
        self.assertEqual(fresh_rung.comment, test_comment)
        comment_element = fresh_rung.element.find("Comment")
        self.assertIsNotNone(comment_element)
        cdata_element = comment_element.find(CDATA_TAG)
        self.assertIsNotNone(cdata_element)
        self.assertEqual(cdata_element.text, test_comment)

    def test_multiple_property_modifications(self):
        """Test multiple property modifications work correctly."""
        self.rung.type = "G"
        self.rung.number = 99
        self.rung.text = "Modified text"
        self.rung.comment = "Modified comment"
        
        self.assertEqual(self.rung.type, "G")
        self.assertEqual(self.rung.number, "99")
        self.assertEqual(self.rung.text, "Modified text")
        self.assertEqual(self.rung.comment, "Modified comment")

    def test_overwrite_existing_cdata_content(self):
        """Test that setting CDATA content overwrites existing content."""
        original_text = self.rung.text
        self.assertIsNotNone(original_text)
        
        new_text = "Completely new text"
        self.rung.text = new_text
        
        self.assertEqual(self.rung.text, new_text)
        self.assertNotEqual(self.rung.text, original_text)








