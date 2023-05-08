"""Contains definitions for styling mixins
"""
from __future__ import annotations
import xml.etree.ElementTree as ET
import enum
from typing import List, Union, Iterable

from .transforms import Affine



class AttributeBase:
    """Base mixin for element attributes
    """

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        For this set of attributes take the data and set them as attributes
        in the xml.etree.ElementTree element. If we have an attribute "colour"
        with a value "green" and the XML tag is called "pentagon" then
        this method would be adding colour="green" to <pentagon colour="green"/>.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        super(AttributeBase, self).set_element_attributes(element)



class Styling(AttributeBase):
    """Styling mixin for attributes style and class
    """
    def __init__(self, style: str = None, cssclass: str = None, **kwargs):
        """Initialise

        Parameters
        ----------
        style : str, optional
            A CSS style name for this part.
        cssclass : str, optional
            A CSS class name for this part.
        """
        self._style = style
        self._cssclass = cssclass
        super(Styling, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the attributes style and class in a tag, for example,
        if this element corresponded to a tag "pentagon" it would set
        <pentagon style="bbb" class="ccc"/>.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._style is not None:
            element.set('style', self._style)
        if self._cssclass is not None:
            element.set('class', self._cssclass)
        super(Styling, self).set_element_attributes(element)


class Transform(AttributeBase):
    """Mixin to store transform attribute
    """

    def __init__(self, transform: Affine=None, **kwargs):
        """Initialise

        Parameters
        ----------
        transform : Affine, optional
            The sequence of affine transformation(s) applied to this part.
        """
        self._transform = transform
        super(Transform, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the transform attribute in the tag, for example,
        if this element corresponded to a tag "pentagon" it would set
        <pentagon transform="xxxx"/>.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._transform is not None:
            element.set('transform', str(self._transform))
        super(Transform, self).set_element_attributes(element)


class LineCap(enum.Enum):
    """How the ends of strokes are drawn.

    Attributes
    ----------
    BUTT
        The edge is squared-off right at the end of the line.
    SQUARE
        The edge is squared-off at the end of the line but extends beyond the end
        of the line by the stroke width.
    ROUND
        The edge is rounded at the end of the line and extends beyond the end of
        the line by the stroke width.
    """
    BUTT = enum.auto()
    SQUARE = enum.auto()
    ROUND = enum.auto()



class LineJoin(enum.Enum):
    """How to mitre joins in lines

    Attributes
    ----------
    ARC
        Line joins are connected with smooth arcs.
    BEVEL
        There is a straight edge perpendicular to the join.
    MITER
        There is a mitre at the join.
    MITER_CLIP
        There is a mitre at the join but the length is clipped.
    ROUND
        There is a rounded cap at the join.
    """
    ARC = enum.auto()
    BEVEL = enum.auto()
    MITER = enum.auto()
    MITER_CLIP = enum.auto()
    ROUND = enum.auto()



class Stroke(AttributeBase):
    """Stroke attributes to apply to a part outline.
    """

    def __init__(self, stroke: str = None,
                    stroke_dash_array: List[float] = None,
                    stroke_dash_offset: float = None,
                    stroke_linecap: LineCap = None,
                    stroke_linejoin: LineJoin = None,
                    stroke_miterlimit: float = None,
                    stroke_opacity: float = None,
                    stroke_width: float = None, **kwargs):
        """Initialise

        Parameters
        ----------
        stroke : str, optional
            Colour for this stroke.  Colour name or hex string.
        stroke_dash_array : List[float], optional
            Array of line lengths and spacings to make a dashed stroke, [2]
            would give a dashed line "--  --  ", whereas [2, 1] would produce
            "-- -- ".
        stroke_dash_offset : float, optional
            Shift the start of the dash pattern of a stroke.
        stroke_linecap : LineCap, optional
            How the ends of the lines are rendered, butt, square or round.
        stroke_linejoin : LineJoin, optional
            How lines are joined together with mitres, bevels, arcs, or rounded joins.
        stroke_miterlimit : float, optional
            If the lines are mitered, how far does the miter extend.
        stroke_opacity : float, optional
            Opacity for the stroke: 0.0 is fully transparent, 1.0 is fully opaque.
        stroke_width : float, optional
            Width of the stroke.
        """
        self._stroke = stroke
        self._stroke_dash_array = stroke_dash_array
        self._stroke_dash_offset = stroke_dash_offset
        self._stroke_linecap = stroke_linecap
        self._stroke_linejoin = stroke_linejoin
        self._stroke_miterlimit = stroke_miterlimit
        self._stroke_opacity = stroke_opacity
        self._stroke_width = stroke_width
        super(Stroke, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the stroke attributes in the tag: "stroke", "stroke-dash-array",
        "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
        "stroke-opacity", and "stroke-width".

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._stroke is not None:
            element.set('stroke', self._stroke)
        if self._stroke_dash_array is not None:
            element.set('stroke-dash-array', ''.join(['{} '.format(x) for x in self._stroke_dash_array]))
        if self._stroke_width is not None:
            element.set('stroke-width', str(self._stroke_width))
        super(Stroke, self).set_element_attributes(element)



class Fill(AttributeBase):
    """Mixing to store fill attributes
    """

    def __init__(self, fill: str = None,
                        fill_opacity: float = None, **kwargs):
        """Initialise

        Parameters
        ----------
        fill : str, optional
            Colour for this fill.  Colour name or hex string.
        fill_opacity : float, optional
            Opacity for the fill: 0.0 is fully transparent, 1.0 is fully opaque.
        """
        self._fill = fill
        self._fill_opacity = fill_opacity
        super(Fill, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the fill attributes in the tag: "fill" and "fill-opacity".

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._fill is not None:
            element.set('fill', self._fill)
        if self._fill_opacity is not None:
            element.set('fill-opacity', self._fill_opacity)
        super(Fill, self).set_element_attributes(element)



class Clip(AttributeBase):
    """Mixin to store clip path
    """

    def __init__(self, clip_path: str=None, **kwargs):
        """Initialise

        Parameters
        ----------
        clip_path : str, optional
            ID of the part that is used as a clip path.
        """
        self._clip_path = clip_path
        super(Clip, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the "clip-path" attribute in the tag.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._clip_path is not None:
            element.set('clip-path', 'url(#'+self._clip_path+')')
        super(Clip, self).set_element_attributes(element)
