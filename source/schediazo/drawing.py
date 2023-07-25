"""All the code for a top-level drawing"""
from typing import Union
import xml.etree.ElementTree as ET
import gzip
import copy

import tinycss2
import tinycss2.ast

from .part import PartDict, PartBase
from .svg import Versions

class Definitions(PartDict):
    """Set of definitions that can be used throughout a drawing.
    """
    def __init__(self):
        super(Definitions,self).__init__()
        self._tag = 'defs'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the clip path under.
        """
        super(Definitions, self).set_element_attributes(element)


class Drawing(PartDict):
    """Drawing
    """
    def __init__(self, **kwargs):
        self._root = None
        self._definitions = Definitions()
        self._styles = []
        super(Drawing, self).__init__(**kwargs)

    def save(self, _filename: str, compressed: bool=False, version: Versions = Versions.SVG11):
        self._root = ET.Element('svg')
        self._root.set('xmlns', 'http://www.w3.org/2000/svg')
        self._root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
        self._root.set('version', version.value)

        # Get dimensions and set width and height.
        #     self._root.set('width', str(self._width))
        #     self._root.set('height', str(self._height))
        #     self._root.set('viewBox', '{} {} {} {}'.format(self._viewbox[0], self._viewbox[1], self._viewbox[2], self._viewbox[3]))

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

        if compressed:
            fh = gzip.open(_filename + '.svgz', mode='wb')
            ET.ElementTree(self._root).write(fh)
        else:
#            ET.indent(self._root, space="\t", level=0)
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
