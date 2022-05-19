"""
This type stub file was generated by pyright.
"""

from docx.opc.part import Part

"""
The proxy class for an image pa"""
class ImagePart(Part):
    """
    An image part. Corresponds """
    def __init__(self, partname, content_type, blob, image=...) -> None:
        ...
    
    @property
    def default_cx(self): # -> Length:
        """
        Native width of this im"""
        ...
    
    @property
    def default_cy(self): # -> Length:
        """
        Native height of this i"""
        ...
    
    @property
    def filename(self): # -> Unknown | str:
        """
        Filename from which thi"""
        ...
    
    @classmethod
    def from_image(cls, image, partname): # -> ImagePart:
        """
        Return an |ImagePart| i"""
        ...
    
    @property
    def image(self): # -> Image:
        ...
    
    @classmethod
    def load(cls, partname, content_type, blob, package): # -> Self@ImagePart:
        """
        Called by ``docx.opc.pa"""
        ...
    
    @property
    def sha1(self): # -> str:
        """
        SHA1 hash digest of the"""
        ...
    


