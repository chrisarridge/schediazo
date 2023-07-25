import xml.etree.ElementTree as ET
from typing import List, Union

import numpy as np

from .attributes import Styling, Stroke, Fill, Transform, Clip, Font, TextRendering
from .part import PartBase
from .paths import RawPath


class Text(TextRendering,Stroke,Fill,Transform,Clip,Styling,Font,PartBase):
    """Text
    """
    def __init__(self, text: str, x: float=None, y: float=None, dx: float=None, dy: float=None,
                        rotate: List[float]=None, **kwargs):
        """Initialise

        Parameters
        ----------
        text : str
            String to render.
        x : float, optional
            X coordinate of the starting point of the text baseline, by default None
        y : float, optional
            X coordinate of the starting point of the text baseline, by default None
        dx : float, optional
            Horizontal shift in starting point of the text baseline from previous text element, by default None
        dy : float, optional
            Vertical shift in starting point of the text baseline from previous text element, by default None
        rotate : List[float], optional
            Rotation angle for each glyph, by default None.
        """
        self._text = text
        self._x = x
        self._y = y
        self._dx = dx
        self._dy = dy
        self._rotate = rotate
        super(Text,self).__init__(**kwargs)
        self._tag = 'text'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the text element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the attributes.
        """
        element.text = self._text
        if self._x is not None:
            element.set('x', str(self._x))
        if self._y is not None:
            element.set('y', str(self._y))
        if self._dx is not None:
            element.set('dx', str(self._dx))
        if self._dy is not None:
            element.set('dy', str(self._dy))
        if self._rotate is not None:
            element.set('rotate', ''.join(['{} '.format(r) for r in self._rotate]))
        super(Text, self).set_element_attributes(element)



class TextPath(TextRendering,Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Text rendered along a path
    """
    def __init__(self, text: str, href: str, side: str=None, start_offset: str=None, path: RawPath=None, **kwargs):
        """Initialise

        Parameters
        ----------
        text : str
            Text to render
        href : str
            URL to path to render text along
        side : str, optional
            Which side of the path is the text rendered on "left" or "right", by default None
        start_offset : str, optional
            Displacement along the path where the text starts, by default None
        path : RawPath, optional
            A path along which the text should be rendered.  If provided the href has no effect.  By default None
        """
        self._text = text
        self._href = href
        self._side = side
        self._start_offset = start_offset
        self._path = path
        super(TextPath,self).__init__(**kwargs)
        self._tag = 'textPath'


    def create_element(self, root: Union[ET.Element,ET.SubElement]) -> ET.SubElement:
        """Create the XML element

        Parameters
        ----------
        root : Union[ET.Element,ET.SubElement]
            XML Element to create this new element under.

        Returns
        -------
        ET.SubElement
            Created XML element.
        """
        base_element = ET.SubElement(root, "text")
        element = ET.SubElement(base_element, self._tag)
        self.set_element_attributes(element)
        return element


    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the textPath element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the attributes.
        """
        element.text = self._text
        if self._href is not None:
            element.set('href', self._href)
        if self._side is not None:
            element.set('side', self._side)
        if self._start_offset is not None:
            element.set('startOffset', self._start_offset)
        if self._path is not None:
            element.set('path', str(self._path))
        super(TextPath, self).set_element_attributes(element)

