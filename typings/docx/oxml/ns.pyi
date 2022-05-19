"""
This type stub file was generated by pyright.
"""

"""
Namespace-related objects.
"""
nsmap = ...
pfxmap = ...
class NamespacePrefixedTag(str):
    """
    Value object that knows the"""
    def __new__(cls, nstag, *args): # -> Self@NamespacePrefixedTag:
        ...
    
    def __init__(self, nstag) -> None:
        ...
    
    @property
    def clark_name(self): # -> str:
        ...
    
    @classmethod
    def from_clark_name(cls, clark_name): # -> Self@NamespacePrefixedTag:
        ...
    
    @property
    def local_part(self):
        """
        Return the local part o"""
        ...
    
    @property
    def nsmap(self): # -> dict[Unknown, str]:
        """
        Return a dict having a """
        ...
    
    @property
    def nspfx(self):
        """
        Return the string names"""
        ...
    
    @property
    def nsuri(self): # -> str:
        """
        Return the namespace UR"""
        ...
    


def nsdecls(*prefixes): # -> str:
    """
    Return a string containing """
    ...

def nspfxmap(*nspfxs): # -> dict[Unknown, str]:
    """
    Return a dict containing th"""
    ...

def qn(tag): # -> str:
    """
    Stands for "qualified name""""
    ...

