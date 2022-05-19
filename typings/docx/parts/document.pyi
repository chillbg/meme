"""
This type stub file was generated by pyright.
"""

from docx.parts.story import BaseStoryPart
from docx.shared import lazyproperty

"""|DocumentPart| and closely relat"""
class DocumentPart(BaseStoryPart):
    """Main document part of a Wordproc"""
    def add_footer_part(self): # -> tuple[FooterPart, Any]:
        """Return (footer_part, rId) pair f"""
        ...
    
    def add_header_part(self): # -> tuple[HeaderPart, Any]:
        """Return (header_part, rId) pair f"""
        ...
    
    @property
    def core_properties(self):
        """
        A |CoreProperties| obje"""
        ...
    
    @property
    def document(self): # -> Document:
        """
        A |Document| object pro"""
        ...
    
    def drop_header_part(self, rId): # -> None:
        """Remove related header part ident"""
        ...
    
    def footer_part(self, rId): # -> Any:
        """Return |FooterPart| related by *"""
        ...
    
    def get_style(self, style_id, style_type): # -> Any | _ParagraphStyle | _CharacterStyle | _TableStyle | _NumberingStyle | None:
        """
        Return the style in thi"""
        ...
    
    def get_style_id(self, style_or_name, style_type): # -> Any | None:
        """
        Return the style_id (|s"""
        ...
    
    def header_part(self, rId): # -> Any:
        """Return |HeaderPart| related by *"""
        ...
    
    @lazyproperty
    def inline_shapes(self): # -> InlineShapes:
        """
        The |InlineShapes| inst"""
        ...
    
    @lazyproperty
    def numbering_part(self): # -> Any:
        """
        A |NumberingPart| objec"""
        ...
    
    def save(self, path_or_stream): # -> None:
        """
        Save this document to *"""
        ...
    
    @property
    def settings(self): # -> Any | Settings:
        """
        A |Settings| object pro"""
        ...
    
    @property
    def styles(self): # -> Any | Styles:
        """
        A |Styles| object provi"""
        ...
    


