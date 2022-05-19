"""
This type stub file was generated by pyright.
"""

"""
Provides a low-level, write-onl"""
class PackageWriter:
    """
    Writes a zip-format OPC pac"""
    @staticmethod
    def write(pkg_file, pkg_rels, parts): # -> None:
        """
        Write a physical packag"""
        ...
    


class _ContentTypesItem:
    """
    Service class that composes"""
    def __init__(self) -> None:
        ...
    
    @property
    def blob(self):
        """
        Return XML form of this"""
        ...
    
    @classmethod
    def from_parts(cls, parts): # -> Self@_ContentTypesItem:
        """
        Return content types XM"""
        ...
    


