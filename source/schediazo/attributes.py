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
            element.set('fill-opacity', str(self._fill_opacity))
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



class FontStyle(enum.Enum):
    """Font styles

    Attributes
    ----------
    Normal
    Italic
    Oblique
    """
    Normal = "normal"
    Italic = "italic"
    Oblique = "oblique"



class FontVariant(enum.Enum):
    """Font variants

    Attributes
    ----------
    Normal
        Normal glyphs
    SmallCaps
        All glyphs are in capitals but lower-case letters are rendered using smaller capital letters.
    AllSmallCaps
        All glyphs are rendered as smaller capital letters.
    PetiteCaps
        All glyphs are in petite capitals but lower-case letters are rendered using smaller petite capital letters.
    AllPetiteCaps
        All glyphs are rendered as smaller petite capital letters.
    Unicase
        Mixed where small capitals are rendered for uppercase letters and normal lowercase letters.
    TitlingCaps
        Capitals for titles.
    """
    Normal = "normal"
    SmallCaps = "small-caps"
    AllSmallCaps = "all-small-caps"
    PetiteCaps = "petite-caps"
    AllPetiteCaps = "all-petite-caps"
    Unicase = "unicase"
    TitlingCaps = "titling-caps"



class FontStretch(enum.Enum):
    """Font stretch

    Attributes
    ----------
    UltraCondensed
    ExtraCondensed
    Condensed
    SemiCondensed
    Normal
    SemiExpanded
    Expanded
    ExtraExpanded
    UltraExpanded
    """
    UltraCondensed = "ultra-condensed"
    ExtraCondensed = "extra-condensed"
    Condensed = "condensed"
    SemiCondensed = "semi-condensed"
    Normal = "normal"
    SemiExpanded = "semi-expanded"
    Expanded = "expanded"
    ExtraExpanded = "extra-expanded"
    UltraExpanded = "ultra-expanded"



class FontWeight(enum.Enum):
    """Font weight

    Attributes
    ----------
    Normal
    Bold
    Lighter
    Bolder
    """
    Normal = "normal"
    Bold = "bold"
    Lighter = "lighter"
    Bolder = "bolder"



class FontSize(enum.Enum):
    """Font sizes

    Attributes
    ----------
    XXSmall
        Extra-extra small absolute font size.
    XSmall
        Extra small absolute font size.
    Small
        Small absolute font size.
    Medium
        Medium absolute font size.
    Large
        Large absolute font size.
    XLarge
        Extra large absolute font size.
    XXLarge
        Extra-extra large absolute font size.
    XXXLarge
        Extra-extra-extra large absolute font size.
    Smaller
        Smaller relative font size (compared to parent element).
    Larger
        Larger relative font size (compared to parent element).
    """
    XXSmall = "xx-small"
    XSmall = "x-small"
    Small = "small"
    Medium = "medium"
    Large = "large"
    XLarge = "x-large"
    XXLarge = "xx-large"
    XXXLarge = "xxx-large"
    Smaller = "smaller"
    Larger = "larger"



class Font(AttributeBase):
    """Mixin to store font information
    """

    def __init__(self, font_family: str=None, font_size: Union[FontSize,str]=None, font_stretch: Union[FontStretch,str]=None,
                 font_style: FontStyle=None, font_variant: FontVariant=None, font_weight: Union[FontWeight,str]=None, **kwargs):
        """Initialise

        Parameters
        ----------
        font_family : str, optional
            Font family string, can give a prioritised string, e.g., "Arial, Helvetica, sans-serif" by default None
        font_size : Union[FontSize,str], optional
            Size of the font, can be a FontSize, or a size string with units, e.g., "12pt", by default None
        font_stretch : Union[FontStretch,str], optional
            Stretching of the font, can be a FontStretch or a string with stretch %, by default None
        font_style : FontStyle, optional
            Style for the string, e.g., italic, by default None
        font_variant : FontVariant, optional
            Variant, e.g., all caps, by default None
        font_weight : Union[FontWeight,str], optional
            Weight, can be a FontWeight, e.g., FontWeight.Bolder, or a size string, e.g., "900", by default None
        """
        self._font_family = font_family
        self._font_size = font_size
        self._font_stretch = font_stretch
        self._font_style = font_style
        self._font_variant = font_variant
        self._font_weight = font_weight
        super(Font, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the font attributes in the tag.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._font_family is not None:
            element.set('font-family', self._font_family)
        if self._font_size is not None:
            if isinstance(self._font_size, FontSize):
                element.set('font-size', self._font_size.value)
            else:
                element.set('font-size', self._font_size)
        if self._font_stretch is not None:
            if isinstance(self._font_stretch, FontStretch):
                element.set('font-stretch', self._font_stretch.value)
            else:
                element.set('font-stretch', self._font_stretch)
        if self._font_style is not None:
            element.set('font-style', self._font_style.value)
        if self._font_variant is not None:
            element.set('font-variant', self._font_variant.value)
        if self._font_weight is not None:
            if isinstance(self._font_weight, FontWeight):
                element.set('font-weight', self._font_weight.value)
            else:
                element.set('font-weight', self._font_weight)
        super(Font, self).set_element_attributes(element)



class TextAnchor(enum.Enum):
    """Text anchoring

    Attributes
    ----------
    Start
    Middle
    End
    """
    Start = "start"
    Middle = "middle"
    End = "end"


class TextRendering(AttributeBase):
    """Mixin to store text rendering information
    """

    def __init__(self, text_anchor: TextAnchor=None, **kwargs):
        """Initialise

        Parameters
        ----------
        text_anchor : TextAnchor, optional
            Anchor point for the for the string, e.g., middle, by default None (start).
        """
        self._text_anchor = text_anchor
        super(TextRendering, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the text rendering attributes in the tag.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        if self._text_anchor is not None:
            if isinstance(self._text_anchor, TextAnchor):
                element.set('text-anchor', self._text_anchor.value)
            else:
                raise ValueError
        super(TextRendering, self).set_element_attributes(element)
