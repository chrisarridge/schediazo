"""All the code for a top-level drawing"""
from typing import Union
import xml.etree.ElementTree as ET
import gzip
import copy

import tinycss2
import tinycss2.ast

import pint

from .units import _tostr
from .part import PartDict, PartBase
from .containers import Definitions
from .svg import Versions
from ._paper import PaperSize



class Drawing(PartDict):
    """Drawing
    """
    def __init__(self, width: pint.Quantity=None, height: pint.Quantity=None, paper: PaperSize=None, orientation: str=None, **kwargs):
        # Do basic type and value checking on inputs.
        if width is not None:
            if not isinstance(width,pint.Quantity):
                raise TypeError("Width must be a number with units (pint.Unit) but received {}".format(type(width)))
        if height is not None:
            if not isinstance(height,pint.Quantity):
                raise TypeError("Height must be a number with units (pint.Unit) but received {}".format(type(height)))
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

            if isinstance(width,(int,float)):
                self._width = float(width)*usr
            else:
                self._width = width
            if isinstance(height,(int,float)):
                self._height = float(height)*usr
            else:
                self._height = height

        super(Drawing, self).__init__(**kwargs)


    def save(self, _filename: str, compressed: bool=False, version: Versions = Versions.SVG11, pretty=False):
        self._root = ET.Element('svg')
        self._root.set('xmlns', 'http://www.w3.org/2000/svg')
        self._root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
        self._root.set('version', version.value)

        # Set the dimensions.
        if self._width is not None:
            self._root.set("width", _tostr(self._width))
        if self._height is not None:
            self._root.set("height", _tostr(self._height))

        # Add all the definition objects.
        if len(self._definitions)>0:
            self._definitions.create_element(self._root)

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
            self[child].create_element(self._root)

        # Write the file.
        if compressed:
            fh = gzip.open(_filename + '.svgz', mode='wb')
            ET.ElementTree(self._root).write(fh)
        else:
            if pretty:
                ET.indent(self._root, space="\t", level=0)
            ET.ElementTree(self._root).write(_filename + '.svg')


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
