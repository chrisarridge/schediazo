"""Contains definitions for styling mixins
"""
from __future__ import annotations
import xml.etree.ElementTree as ET
import enum
from typing import List, Union, Iterable

import pint

from .transforms import Affine
from .units import _tostr, ureg
from .maths import clip

class AttributeBase:
    """Base mixin for element attributes
    """

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        For this set of attributes take the data and set them as attributes
        in the xml.etree.ElementTree element. If we have an attribute "colour"
        with a value "green" and the XML tag is called "pentagon" then
        this method would be adding colour="green" to <pentagon colour="green"/>.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        super(AttributeBase, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



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
        if style is not None:
            if not isinstance(style,str):
                raise TypeError("Style should be a string")
        if cssclass is not None:
            if not isinstance(cssclass,str):
                raise TypeError("CSS Id should be a string")
        self._style = style
        self._cssclass = cssclass
        super(Styling, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the attributes style and class in a tag, for example,
        if this element corresponded to a tag "pentagon" it would set
        <pentagon style="bbb" class="ccc"/>.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._style is not None:
            element.set('style', self._style)
        if self._cssclass is not None:
            element.set('class', self._cssclass)
        super(Styling, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)


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
        if transform is not None and not isinstance(transform,Affine):
            raise TypeError("transform must be a schediazo.transforms.Affine object.")
        self._transform = transform

        super(Transform, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the transform attribute in the tag, for example,
        if this element corresponded to a tag "pentagon" it would set
        <pentagon transform="xxxx"/>.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._transform is not None:
            element.set('transform', str(self._transform))
        super(Transform, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)


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
    BUTT = "butt"
    SQUARE = "square"
    ROUND = "round"



class LineJoin(enum.Enum):
    """How to mitre joins in lines

    Attributes
    ----------
    ARCS
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
    ARCS = "arcs"
    BEVEL = "bevel"
    MITER = "miter"
    MITER_CLIP = "miter-clip"
    ROUND = "round"

class Stroke(AttributeBase):
    """Stroke attributes to apply to a part outline.
    """

    def __init__(self, stroke: str = None,
                    stroke_dash_array: List[pint.Quantity] = None,
                    stroke_dash_offset: pint.Quantity = None,
                    stroke_linecap: LineCap = None,
                    stroke_linejoin: LineJoin = None,
                    stroke_miterlimit: float = None,
                    stroke_opacity: float = None,
                    stroke_width: pint.Quantity = None, **kwargs):
        """Initialise

        Parameters
        ----------
        stroke : str, optional
            Colour for this stroke.  Colour name or hex string.
        stroke_dash_array : List[pint.Quantity], optional
            Array of line lengths and spacings to make a dashed stroke, [2]
            would give a dashed line "--  --  ", whereas [2, 1] would produce
            "-- -- ".
        stroke_dash_offset : pint.Quantity, optional
            Shift the start of the dash pattern of a stroke.
        stroke_linecap : LineCap, optional
            How the ends of the lines are rendered, butt, square or round.
        stroke_linejoin : LineJoin, optional
            How lines are joined together with mitres, bevels, arcs, or rounded joins.
        stroke_miterlimit : float, optional
            If the lines are mitered, how far does the miter extend.
        stroke_opacity : float, optional
            Opacity for the stroke: 0.0 is fully transparent, 1.0 is fully opaque.
        stroke_width : pint.Quantity, optional
            Width of the stroke.
        """
        # Check types and units
        if stroke is not None and not isinstance(stroke,str):
            raise TypeError("Stroke colour must be a string")
        self._stroke = stroke

        if stroke_dash_array is not None:
            if not isinstance(stroke_dash_array,list):
                raise TypeError("Stroke dash array must be a list of pint.Quantities")
            for x in stroke_dash_array:
                if not isinstance(x,pint.Quantity):
                    raise TypeError("Stroke dash array must be a list of pint.Quantities")
        self._stroke_dash_array = stroke_dash_array

        if stroke_dash_offset is not None:
            if not isinstance(stroke_dash_offset,pint.Quantity):
                raise TypeError("Stroke dash offset must be a pint.Quantity")
        self._stroke_dash_offset = stroke_dash_offset

        if stroke_linecap is not None and not isinstance(stroke_linecap,LineCap):
            raise TypeError("Stroke line cap must be a LineCap object")
        self._stroke_linecap = stroke_linecap

        if stroke_linejoin is not None and not isinstance(stroke_linejoin,LineJoin):
            raise TypeError("Stroke line join must be a LineJoin object")
        self._stroke_linejoin = stroke_linejoin

        if stroke_miterlimit is not None and not isinstance(stroke_miterlimit,float):
            raise TypeError("Stroke miter limit must be a floating point number")
        self._stroke_miterlimit = stroke_miterlimit

        if stroke_opacity is not None:
            if not isinstance(stroke_opacity,float):
                raise TypeError("Stroke opacity must be a floating point number")
            self._stroke_opacity = clip(stroke_opacity, 0.0, 1.0)
        else:
            self._stroke_opacity = None

        if stroke_width is not None:
            if not isinstance(stroke_width,pint.Quantity):
                raise TypeError("Stroke width must be a pint.Quantity with [length] or [pixel] units")
            if not (stroke_width.check("[length]") or stroke_width.check("[pixel]")):
                raise ValueError("Stroke width must be a pint.Quantity with [length] or [pixel] units")
        self._stroke_width = stroke_width

        super(Stroke, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the stroke attributes in the tag: "stroke", "stroke-dash-array",
        "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
        "stroke-opacity", and "stroke-width".

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._stroke is not None:
            element.set('stroke', self._stroke)
        if self._stroke_dash_array is not None:
            element.set('stroke-dasharray', ''.join(['{} '.format(_tostr(x)) for x in self._stroke_dash_array]))
        if self._stroke_dash_offset is not None:
            element.set('stroke-dashoffset', _tostr(self._stroke_dash_offset))
        if self._stroke_linecap is not None:
            element.set('stroke-linecap', self._stroke_linecap.value)
        if self._stroke_linejoin is not None:
            element.set('stroke-linejoin', self._stroke_linejoin.value)
        if self._stroke_miterlimit is not None:
            element.set('stroke-miterlimit', str(self._stroke_miterlimit))
        if self._stroke_opacity is not None:
            element.set('stroke-opacity', str(self._stroke_opacity))
        if self._stroke_width is not None:
            element.set('stroke-width', _tostr(self._stroke_width))

        super(Stroke, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



class Fill(AttributeBase):
    """Mixing to store fill attributes
    """

    def __init__(self, fill: str = "none",
                        fill_opacity: float = None, **kwargs):
        """Initialise

        Parameters
        ----------
        fill : str, optional
            Colour for this fill.  Colour name or hex string.  Default is "none".
        fill_opacity : float, optional
            Opacity for the fill: 0.0 is fully transparent, 1.0 is fully opaque.
        """
        if not isinstance(fill,str):
            raise TypeError("Fill colour must be a string")
        self._fill = fill

        if fill_opacity is not None:
            if not isinstance(fill_opacity,float):
                raise TypeError("Fill opacity must be a floating point number")
            self._fill_opacity = clip(fill_opacity, 0.0, 1.0)
        else:
            self._fill_opacity = None

        super(Fill, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the fill attributes in the tag: "fill" and "fill-opacity".

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._fill is not None:
            element.set('fill', self._fill)
        if self._fill_opacity is not None:
            element.set('fill-opacity', str(self._fill_opacity))

        super(Fill, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



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
        if clip_path is not None and not isinstance(clip_path,str):
            raise TypeError("clip_path should be a string")
        self._clip_path = clip_path

        super(Clip, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the "clip-path" attribute in the tag.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._clip_path is not None:
            element.set('clip-path', 'url(#'+self._clip_path+')')

        super(Clip, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



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

    def __init__(self, font_family: str=None, font_size: Union[FontSize,pint.Quantity]=None,
                font_stretch: Union[FontStretch,pint.Quantity]=None, font_style: FontStyle=None,
                font_variant: FontVariant=None, font_weight: Union[FontWeight,int]=None, **kwargs):
        """Initialise

        Parameters
        ----------
        font_family : str, optional
            Font family string, can give a prioritised string, e.g., "Arial, Helvetica, sans-serif" by default None
        font_size : Union[FontSize,pint.Quantity], optional
            Size of the font, can be a FontSize, or a pint.Quantity giving the size with units, by default None
        font_stretch : Union[FontStretch,pint.Quantity], optional
            Stretching of the font, can be a FontStretch or pint.Quantity giving the percentage stretch, by default None
        font_style : FontStyle, optional
            Style for the string, e.g., italic, by default None
        font_variant : FontVariant, optional
            Variant, e.g., all caps, by default None
        font_weight : Union[FontWeight,int,float], optional
            Weight, can be a FontWeight, e.g., FontWeight.Bolder, or a size value, e.g., 900, by default None
        """
        if font_family is not None and not isinstance(font_family,str):
            raise TypeError("Font family must be a string")
        self._font_family = font_family

        if font_size is not None and not isinstance(font_size,(FontSize,pint.Quantity)):
            raise TypeError("Font size must be a FontSize object or a pint.Quantity")
        self._font_size = font_size

        if font_stretch is not None:
            if not isinstance(font_stretch,(FontStretch,pint.Quantity)):
                raise TypeError("Font stretch must be a FontStretch object or a pint.Quantity with percentage units")
            if isinstance(font_stretch,pint.Quantity):
                if not font_stretch.check("[percentage]"):
                    raise ValueError("Font stretch must be a FontStretch object or a pint.Quantity with percentage units")
        self._font_stretch = font_stretch

        if font_style is not None and not isinstance(font_style,FontStyle):
            raise TypeError("Font style must be a FontStyle object")
        self._font_style = font_style

        if font_variant is not None and not isinstance(font_variant,FontVariant):
            raise TypeError("Font variant must be a FontVariant object")
        self._font_variant = font_variant

        if font_weight is not None:
            if not isinstance(font_weight,(FontWeight,int)):
                raise TypeError("Font weight must be a FontWeight object or a positive integer number")
            if isinstance(font_weight, int):
                if font_weight<0:
                    raise ValueError("Font weight must be a FontWeight object or a positive integer number")
        self._font_weight = font_weight

        super(Font, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the font attributes in the tag.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._font_family is not None:
            element.set('font-family', self._font_family)

        if self._font_size is not None:
            if isinstance(self._font_size, FontSize):
                element.set('font-size', self._font_size.value)
            else:
                element.set('font-size', _tostr(self._font_size))

        if self._font_stretch is not None:
            if isinstance(self._font_stretch, FontStretch):
                element.set('font-stretch', self._font_stretch.value)
            else:
                element.set('font-stretch', _tostr(self._font_stretch))

        if self._font_style is not None:
            element.set('font-style', self._font_style.value)

        if self._font_variant is not None:
            element.set('font-variant', self._font_variant.value)

        if self._font_weight is not None:
            if isinstance(self._font_weight, FontWeight):
                element.set('font-weight', self._font_weight.value)
            else:
                element.set('font-weight', str(self._font_weight))

        super(Font, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



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
        if text_anchor is not None and not isinstance(text_anchor,TextAnchor):
            raise TypeError("Text anchor must be a TextAnchor object")
        self._text_anchor = text_anchor

        super(TextRendering, self).__init__(**kwargs)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the text rendering attributes in the tag.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        if self._text_anchor is not None:
            element.set('text-anchor', self._text_anchor.value)

        super(TextRendering, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)
