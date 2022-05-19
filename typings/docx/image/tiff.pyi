"""
This type stub file was generated by pyright.
"""

from .image import BaseImageHeader

class Tiff(BaseImageHeader):
    """
    Image header parser for TIF"""
    @property
    def content_type(self): # -> Literal['image/tiff']:
        """
        Return the MIME type of"""
        ...
    
    @property
    def default_ext(self): # -> Literal['tiff']:
        """
        Default filename extens"""
        ...
    
    @classmethod
    def from_stream(cls, stream): # -> Self@Tiff:
        """
        Return a |Tiff| instanc"""
        ...
    


class _TiffParser:
    """
    Parses a TIFF image stream """
    def __init__(self, ifd_entries) -> None:
        ...
    
    @classmethod
    def parse(cls, stream): # -> Self@_TiffParser:
        """
        Return an instance of |"""
        ...
    
    @property
    def horz_dpi(self): # -> int:
        """
        The horizontal dots per"""
        ...
    
    @property
    def vert_dpi(self): # -> int:
        """
        The vertical dots per i"""
        ...
    
    @property
    def px_height(self):
        """
        The number of stacked r"""
        ...
    
    @property
    def px_width(self):
        """
        The number of pixels in"""
        ...
    


class _IfdEntries:
    """
    Image File Directory for a """
    def __init__(self, entries) -> None:
        ...
    
    def __contains__(self, key):
        """
        Provides ``in`` operato"""
        ...
    
    def __getitem__(self, key):
        """
        Provides indexed access"""
        ...
    
    @classmethod
    def from_stream(cls, stream, offset): # -> Self@_IfdEntries:
        """
        Return a new |_IfdEntri"""
        ...
    
    def get(self, tag_code, default=...):
        """
        Return value of IFD ent"""
        ...
    


class _IfdParser:
    """
    Service object that knows h"""
    def __init__(self, stream_rdr, offset) -> None:
        ...
    
    def iter_entries(self): # -> Generator[_AsciiIfdEntry | _ShortIfdEntry | _LongIfdEntry | _RationalIfdEntry | _IfdEntry, None, None]:
        """
        Generate an |_IfdEntry|"""
        ...
    


class _IfdEntry:
    """
    Base class for IFD entry cl"""
    def __init__(self, tag_code, value) -> None:
        ...
    
    @classmethod
    def from_stream(cls, stream_rdr, offset): # -> Self@_IfdEntry:
        """
        Return an |_IfdEntry| s"""
        ...
    
    @property
    def tag(self): # -> Unknown:
        """
        Short int code that ide"""
        ...
    
    @property
    def value(self): # -> Unknown:
        """
        Value of this tag, its """
        ...
    


class _AsciiIfdEntry(_IfdEntry):
    """
    IFD entry having the form o"""
    ...


class _ShortIfdEntry(_IfdEntry):
    """
    IFD entry expressed as a sh"""
    ...


class _LongIfdEntry(_IfdEntry):
    """
    IFD entry expressed as a lo"""
    ...


class _RationalIfdEntry(_IfdEntry):
    """
    IFD entry expressed as a nu"""
    ...


