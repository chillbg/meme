"""
This type stub file was generated by pyright.
"""

from lxml import etree
from docx.compat import Unicode

"""
Provides a wrapper around lxml """
def serialize_for_reading(element): # -> XmlString:
    """
    Serialize *element* to huma"""
    ...

class XmlString(Unicode):
    """
    Provides string comparison """
    _xml_elm_line_patt = ...
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class MetaOxmlElement(type):
    """
    Metaclass for BaseOxmlEleme"""
    def __init__(cls, clsname, bases, clsdict) -> None:
        ...
    


class BaseAttribute:
    """
    Base class for OptionalAttr"""
    def __init__(self, attr_name, simple_type) -> None:
        ...
    
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Add the appropriate met"""
        ...
    


class OptionalAttribute(BaseAttribute):
    """
    Defines an optional attribu"""
    def __init__(self, attr_name, simple_type, default=...) -> None:
        ...
    


class RequiredAttribute(BaseAttribute):
    """
    Defines a required attribut"""
    ...


class _BaseChildElement:
    """
    Base class for the child el"""
    def __init__(self, nsptagname, successors=...) -> None:
        ...
    
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Baseline behavior for a"""
        ...
    


class Choice(_BaseChildElement):
    """
    Defines a child element bel"""
    @property
    def nsptagname(self): # -> Unknown:
        ...
    
    def populate_class_members(self, element_cls, group_prop_name, successors): # -> None:
        """
        Add the appropriate met"""
        ...
    


class OneAndOnlyOne(_BaseChildElement):
    """
    Defines a required child el"""
    def __init__(self, nsptagname) -> None:
        ...
    
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Add the appropriate met"""
        ...
    


class OneOrMore(_BaseChildElement):
    """
    Defines a repeating child e"""
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Add the appropriate met"""
        ...
    


class ZeroOrMore(_BaseChildElement):
    """
    Defines an optional repeati"""
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Add the appropriate met"""
        ...
    


class ZeroOrOne(_BaseChildElement):
    """
    Defines an optional child e"""
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Add the appropriate met"""
        ...
    


class ZeroOrOneChoice(_BaseChildElement):
    """
    Correspondes to an ``EG_*``"""
    def __init__(self, choices, successors=...) -> None:
        ...
    
    def populate_class_members(self, element_cls, prop_name): # -> None:
        """
        Add the appropriate met"""
        ...
    


class _OxmlElementBase(etree.ElementBase):
    """
    Effective base class for al"""
    __metaclass__ = MetaOxmlElement
    def __repr__(self): # -> str:
        ...
    
    def first_child_found_in(self, *tagnames): # -> None:
        """
        Return the first child """
        ...
    
    def insert_element_before(self, elm, *tagnames):
        ...
    
    def remove_all(self, *tagnames): # -> None:
        """
        Remove all child elemen"""
        ...
    
    @property
    def xml(self): # -> XmlString:
        """
        Return XML string for t"""
        ...
    
    def xpath(self, xpath_str):
        """
        Override of ``lxml`` _E"""
        ...
    


BaseOxmlElement = ...
