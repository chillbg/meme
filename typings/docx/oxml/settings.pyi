"""
This type stub file was generated by pyright.
"""

from docx.oxml.xmlchemy import BaseOxmlElement

"""Custom element classes related t"""
class CT_Settings(BaseOxmlElement):
    """`w:settings` element, root eleme"""
    _tag_seq = ...
    evenAndOddHeaders = ...
    @property
    def evenAndOddHeaders_val(self): # -> Literal[False]:
        """value of `w:evenAndOddHeaders/@w"""
        ...
    
    @evenAndOddHeaders_val.setter
    def evenAndOddHeaders_val(self, value): # -> None:
        ...
    


