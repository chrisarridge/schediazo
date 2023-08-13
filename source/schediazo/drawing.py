"""All the code for a top-level drawing"""
from typing import Union
import xml.etree.ElementTree as ET
import gzip
import copy

import tinycss2
import tinycss2.ast

import pint

from .units import _tostr, px, inch, ureg
from .part import PartDict, PartBase
from .containers import Definitions
from .paper import PaperSize



class Drawing(PartDict):
    """Drawing
    """
    def __init__(self, width: pint.Quantity=None, height: pint.Quantity=None, paper: PaperSize=None, orientation: str=None, **kwargs):
        """Initialise a new drawing.

        Parameters
        ----------
        width : pint.Quantity, optional
            Width of the drawing, by default None
        height : pint.Quantity, optional
            Height of the drawing, by default None
        paper : PaperSize, optional
            Standard papersize definition to automatically set width and height, by default None.  Will
            be overriden by manually specified widths and heights.
        orientation : str, optional
            "portrait" or "landscape", by default None which forces a paper specification to use the defined orientation.

        Raises
        ------
        TypeError
            If width, height, paper or orientation do not have the correct type.
        """
        # Do basic type and value checking on inputs.
        if width is not None:
            if not isinstance(width,pint.Quantity):
                raise TypeError("Width must be a number with units (pint.Unit) but received {}".format(type(width)))
            if not (width.check('[length]') or width.check('[pixel]')):
                raise ValueError("Width must be a length or number of pixels")

        if height is not None:
            if not isinstance(height,pint.Quantity):
                raise TypeError("Height must be a number with units (pint.Unit) but received {}".format(type(height)))
            if not (height.check('[length]') or height.check('[pixel]')):
                raise ValueError("Height must be a length or number of pixels")
        if width is None and height is not None:
            print("Provided with height but no width - ignoring size specification")
        if width is not None and height is None:
            print("Provided with width but no height - ignoring size specification")
        if paper is not None:
            if not isinstance(paper, PaperSize):
                raise TypeError("Not a PaperSize value")
        if orientation is not None:
            if not isinstance(orientation, str):
                raise TypeError("Orientation must be a string")
            if not (orientation=="portrait" or orientation=="landscape"):
                raise TypeError("Orientation must be portrait or landscape")

        # Setup basic elements of the object.
        self._root = None
        self._definitions = Definitions()
        self._styles = []

        # Set the width and height.
        self._width = None
        self._height = None

        if paper is not None:
            # PaperSize tuples are portrait by definition
            self._width = paper.value[0]
            self._height = paper.value[1]

            if orientation is not None:
                if orientation=="landscape":
                    self._width = paper.value[1]
                    self._height = paper.value[0]

        if width is not None and height is not None:
            if paper is not None:
                print("Provided both width/height and a PaperSize, ignoring the PaperSize")

            self._width = width
            self._height = height

        # Set default scalings to device units.
        self._device_per_length = 72*ureg.device/ureg.inch
        self._device_per_pixel = 1*ureg.device/ureg.px

        super(Drawing, self).__init__(**kwargs)

    @property
    def device_per_length(self) -> pint.Quantity:
        """Return device per unit length scaling

        Returns
        -------
        pint.Quantity
        """
        return self._device_per_length

    @device_per_length.setter
    def device_per_length(self, x: pint.Quantity):
        """Set new device per unit length

        Parameters
        ----------
        x : pint.Quantity
            New device per unit length scaling, e.g., 72 device units per inch

        Raises
        ------
        TypeError
            If new scaling is not a pint.Quantity
        ValueError
            if new scaling does not have the correct units.
        """
        if not isinstance(x, pint.Quantity):
            raise TypeError("device per unit length must be a pint.Quantity")
        if not x.check("[device]/[length]"):
            raise ValueError("device per unit length must have dimensions of device units per length")
        self._device_per_length = x

    @property
    def device_per_pixel(self):
        """Return device per pixel scaling

        Returns
        -------
        pint.Quantity
        """
        return self._device_per_pixel

    @device_per_pixel.setter
    def device_per_pixel(self, x: pint.Quantity):
        """Set new device per pixel

        Parameters
        ----------
        x : pint.Quantity
            New device per pixel scaling, e.g., 2 device units per pixel

        Raises
        ------
        TypeError
            If new scaling is not a pint.Quantity
        ValueError
            if new scaling does not have the correct units.
        """
        if not isinstance(x, pint.Quantity):
            raise TypeError("device per pixel must be a pint.Quantity")
        if not x.check("[device]/[pixel]"):
            raise ValueError("device per pixel must have dimensions of device units per pixel")
        self._device_per_pixel = x


    def save(self, _filename: str, compressed: bool=False, pretty: bool=False):
        """Save drawing to an SVG file.

        Parameters
        ----------
        _filename : str
            Filename, can have a .svg or .svgz extension but will be added/corrected.
        compressed : bool, optional
            Write a compressed or uncompressed SVG file, by default False
        pretty : bool, optional
            Whether to pretty the XML output, by default False

        Raises
        ------
        TypeError
            If inputs do not have the correct type.
        """
        if not isinstance(_filename,str):
            raise TypeError("Filename must be a string")
        if not isinstance(compressed, bool):
            raise TypeError("compressed must be a boolean")
        if not isinstance(pretty, bool):
            raise TypeError("pretty must be a boolean")

        # Figure out filename.
        if _filename[-4:0]==".svg" or _filename[-5:0]==".svgz":
            if _filename[-4:0]==".svg" and compressed:
                filename = _filename + "z"
            elif _filename[-5:0]==".svgz" and not compressed:
                filename = _filename[:-1]
            else:
                filename = _filename
        else:
            if compressed:
                filename = _filename + ".svgz"
            else:
                filename = _filename + ".svg"

        # Setup the root SVG element.
        self._root = ET.Element('svg')
        self._root.set('xmlns', 'http://www.w3.org/2000/svg')
        self._root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
        self._root.set('version', "1.1")

        # Set the dimensions.
        if self._width is not None:
            self._root.set("width", _tostr(self._width))
        if self._height is not None:
            self._root.set("height", _tostr(self._height))

        # Add all the definition objects.
        if len(self._definitions)>0:
            self._definitions.create_element(self._root, device_per_length=self._device_per_length, device_per_pixel=self._device_per_pixel)

        # Add the styles.
        if len(self._styles)>0:
            element = ET.SubElement(self._root, "style")

            sheet = []
            for x in self._styles:
                if not isinstance(x,(tinycss2.tokenizer.Comment,tinycss2.tokenizer.WhitespaceToken)):
                    if isinstance(x,tinycss2.ast.QualifiedRule):
                        tmp = copy.copy(x)
                        tmp.prelude = [_x for _x in tmp.prelude if not isinstance(_x,(tinycss2.ast.Comment,tinycss2.ast.WhitespaceToken))]
                        tmp.content = [_x for _x in tmp.content if not isinstance(_x,(tinycss2.ast.Comment,tinycss2.ast.WhitespaceToken))]
                        sheet.append(tmp)
            element.text = tinycss2.serialize(sheet)

        # Add the other objects.
        for child in self:
            self[child].create_element(self._root, device_per_length=self._device_per_length, device_per_pixel=self._device_per_pixel)

        # Write the file.
        if compressed:
            fh = gzip.open(filename, mode='wb')
            ET.ElementTree(self._root).write(fh)
        else:
            if pretty:
                ET.indent(self._root, space="\t", level=0)
            ET.ElementTree(self._root).write(filename)


    def add_def(self, part: Union[PartBase,PartDict]):
        """Add a definition to the drawing.

        Parameters
        ----------
        part : Union[PartBase,PartDict]
            The part to add as a definition.
        """
        self._definitions.add(part)


    def add_style(self, style_string: str):
        """Parses a string of CSS and adds it to the list of styles

        Parameters
        ----------
        style_string : str
            Valid string of CSS.
        """
        self._styles += tinycss2.parse_stylesheet(style_string)
