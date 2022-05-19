"""
This type stub file was generated by pyright.
"""

from docx.blkcntnr import BlockItemContainer
from docx.compat import Sequence
from docx.shared import lazyproperty

"""The |Section| object and related"""
class Sections(Sequence):
    """Sequence of |Section| objects co"""
    def __init__(self, document_elm, document_part) -> None:
        ...
    
    def __getitem__(self, key): # -> list[Section] | Section:
        ...
    
    def __iter__(self): # -> Generator[Section, None, None]:
        ...
    
    def __len__(self): # -> int:
        ...
    


class Section:
    """Document section, providing acce"""
    def __init__(self, sectPr, document_part) -> None:
        ...
    
    @property
    def bottom_margin(self):
        """
        |Length| object represe"""
        ...
    
    @bottom_margin.setter
    def bottom_margin(self, value): # -> None:
        ...
    
    @property
    def different_first_page_header_footer(self):
        """True if this section displays a """
        ...
    
    @different_first_page_header_footer.setter
    def different_first_page_header_footer(self, value): # -> None:
        ...
    
    @property
    def even_page_footer(self): # -> _Footer:
        """|_Footer| object defining footer"""
        ...
    
    @property
    def even_page_header(self): # -> _Header:
        """|_Header| object defining header"""
        ...
    
    @property
    def first_page_footer(self): # -> _Footer:
        """|_Footer| object defining footer"""
        ...
    
    @property
    def first_page_header(self): # -> _Header:
        """|_Header| object defining header"""
        ...
    
    @lazyproperty
    def footer(self): # -> _Footer:
        """|_Footer| object representing de"""
        ...
    
    @property
    def footer_distance(self):
        """
        |Length| object represe"""
        ...
    
    @footer_distance.setter
    def footer_distance(self, value): # -> None:
        ...
    
    @property
    def gutter(self):
        """
        |Length| object represe"""
        ...
    
    @gutter.setter
    def gutter(self, value): # -> None:
        ...
    
    @lazyproperty
    def header(self): # -> _Header:
        """|_Header| object representing de"""
        ...
    
    @property
    def header_distance(self):
        """
        |Length| object represe"""
        ...
    
    @header_distance.setter
    def header_distance(self, value): # -> None:
        ...
    
    @property
    def left_margin(self):
        """
        |Length| object represe"""
        ...
    
    @left_margin.setter
    def left_margin(self, value): # -> None:
        ...
    
    @property
    def orientation(self):
        """
        Member of the :ref:`WdO"""
        ...
    
    @orientation.setter
    def orientation(self, value): # -> None:
        ...
    
    @property
    def page_height(self):
        """
        Total page height used """
        ...
    
    @page_height.setter
    def page_height(self, value): # -> None:
        ...
    
    @property
    def page_width(self):
        """
        Total page width used f"""
        ...
    
    @page_width.setter
    def page_width(self, value): # -> None:
        ...
    
    @property
    def right_margin(self):
        """
        |Length| object represe"""
        ...
    
    @right_margin.setter
    def right_margin(self, value): # -> None:
        ...
    
    @property
    def start_type(self):
        """
        The member of the :ref:"""
        ...
    
    @start_type.setter
    def start_type(self, value): # -> None:
        ...
    
    @property
    def top_margin(self):
        """
        |Length| object represe"""
        ...
    
    @top_margin.setter
    def top_margin(self, value): # -> None:
        ...
    


class _BaseHeaderFooter(BlockItemContainer):
    """Base class for header and footer"""
    def __init__(self, sectPr, document_part, header_footer_index) -> None:
        ...
    
    @property
    def is_linked_to_previous(self): # -> bool:
        """``True`` if this header/footer u"""
        ...
    
    @is_linked_to_previous.setter
    def is_linked_to_previous(self, value): # -> None:
        ...
    
    @property
    def part(self):
        """The |HeaderPart| or |FooterPart|"""
        ...
    


class _Footer(_BaseHeaderFooter):
    """Page footer, used for all three """
    ...


class _Header(_BaseHeaderFooter):
    """Page header, used for all three """
    ...


