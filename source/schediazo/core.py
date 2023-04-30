from typing import List
import enum
import gzip
import xml.etree.ElementTree as ET


class Versions(enum.Enum):
    SVG10 = "1.0"
    SVG11 = "1.1"
    SVG20 = "2.0"


class Drawing:
    def __init__(self, width: float = None, height: float = None, viewbox: List[float] = None, version: Versions=Versions.SVG11):
        self._root = ET.Element('svg')
        self._root.set('xmlns', 'http://www.w3.org/2000/svg')
        self._root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
        self._root.set('version', version.value)
        self._width = width
        self._height = height
        self._viewbox = viewbox

        self._objects = []
        self._defs = []


    def finalise(self):
        # Add all the definition objects.
        defs = ET.SubElement(self._root, 'defs')
        for o in self._defs:
            o.create_element(defs)

        # Add all the objects to the tree.
        for o in self._objects:
            o.create_element(self._root)

        # Set the SVG attributes.        
        if self._width is not None:
            self._root.set('width', str(self._width))

        if self._height is not None:
            self._root.set('height', str(self._height))

        if self._viewbox is not None:
            self._root.set('viewBox', '{} {} {} {}'.format(self._viewbox[0], self._viewbox[1], self._viewbox[2], self._viewbox[3]))


    def save(self, _filename, compressed=False):
        if compressed:
            fh = gzip.open(_filename + '.svgz', mode='wb')
            ET.ElementTree(self._root).write(fh)
        else:
#            ET.indent(self._root, space="\t", level=0)
            ET.ElementTree(self._root).write(_filename + '.svg')

    def add(self, obj):
        self._objects.append(obj)
        return obj

    def add_def(self, obj):
        self._defs.append(obj)
        return obj

