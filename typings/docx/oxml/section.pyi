"""
This type stub file was generated by pyright.
"""

from docx.oxml.xmlchemy import BaseOxmlElement

"""Section-related custom element c"""
class CT_HdrFtr(BaseOxmlElement):
    """`w:hdr` and `w:ftr`, the root el"""
    p = ...
    tbl = ...


class CT_HdrFtrRef(BaseOxmlElement):
    """`w:headerReference` and `w:foote"""
    type_ = ...
    rId = ...


class CT_PageMar(BaseOxmlElement):
    """
    ``<w:pgMar>`` element, defi"""
    top = ...
    right = ...
    bottom = ...
    left = ...
    header = ...
    footer = ...
    gutter = ...


class CT_PageSz(BaseOxmlElement):
    """
    ``<w:pgSz>`` element, defin"""
    w = ...
    h = ...
    orient = ...


class CT_SectPr(BaseOxmlElement):
    """`w:sectPr` element, the containe"""
    _tag_seq = ...
    headerReference = ...
    footerReference = ...
    type = ...
    pgSz = ...
    pgMar = ...
    titlePg = ...
    def add_footerReference(self, type_, rId):
        """Return newly added CT_HdrFtrRef """
        ...
    
    def add_headerReference(self, type_, rId):
        """Return newly added CT_HdrFtrRef """
        ...
    
    @property
    def bottom_margin(self): # -> None:
        """
        The value of the ``w:bo"""
        ...
    
    @bottom_margin.setter
    def bottom_margin(self, value): # -> None:
        ...
    
    def clone(self): # -> Self@CT_SectPr:
        """
        Return an exact duplica"""
        ...
    
    @property
    def footer(self): # -> None:
        """
        The value of the ``w:fo"""
        ...
    
    @footer.setter
    def footer(self, value): # -> None:
        ...
    
    def get_footerReference(self, type_): # -> None:
        """Return footerReference element o"""
        ...
    
    def get_headerReference(self, type_): # -> None:
        """Return headerReference element o"""
        ...
    
    @property
    def gutter(self): # -> None:
        """
        The value of the ``w:gu"""
        ...
    
    @gutter.setter
    def gutter(self, value): # -> None:
        ...
    
    @property
    def header(self): # -> None:
        """
        The value of the ``w:he"""
        ...
    
    @header.setter
    def header(self, value): # -> None:
        ...
    
    @property
    def left_margin(self): # -> None:
        """
        The value of the ``w:le"""
        ...
    
    @left_margin.setter
    def left_margin(self, value): # -> None:
        ...
    
    @property
    def orientation(self):
        """
        The member of the ``WD_"""
        ...
    
    @orientation.setter
    def orientation(self, value): # -> None:
        ...
    
    @property
    def page_height(self): # -> None:
        """
        Value in EMU of the ``h"""
        ...
    
    @page_height.setter
    def page_height(self, value): # -> None:
        ...
    
    @property
    def page_width(self): # -> None:
        """
        Value in EMU of the ``w"""
        ...
    
    @page_width.setter
    def page_width(self, value): # -> None:
        ...
    
    @property
    def preceding_sectPr(self): # -> None:
        """sectPr immediately preceding thi"""
        ...
    
    def remove_footerReference(self, type_):
        """Return rId of w:footerReference """
        ...
    
    def remove_headerReference(self, type_):
        """Return rId of w:headerReference """
        ...
    
    @property
    def right_margin(self): # -> None:
        """
        The value of the ``w:ri"""
        ...
    
    @right_margin.setter
    def right_margin(self, value): # -> None:
        ...
    
    @property
    def start_type(self):
        """
        The member of the ``WD_"""
        ...
    
    @start_type.setter
    def start_type(self, value): # -> None:
        ...
    
    @property
    def titlePg_val(self): # -> Literal[False]:
        """Value of `w:titlePg/@val` or |No"""
        ...
    
    @titlePg_val.setter
    def titlePg_val(self, value): # -> None:
        ...
    
    @property
    def top_margin(self): # -> None:
        """
        The value of the ``w:to"""
        ...
    
    @top_margin.setter
    def top_margin(self, value): # -> None:
        ...
    


class CT_SectType(BaseOxmlElement):
    """
    ``<w:sectType>`` element, d"""
    val = ...


