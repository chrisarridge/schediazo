import xml.etree.ElementTree as ET
from typing import Union

from .elements import Element, Core, Stroke, Fill, Transform, Clip


class Path(Stroke,Fill,Transform,Clip,Core,Element):
    """Path shape"""
    def __init__(self, **kwargs):
        self._commands = []
        super(Path,self).__init__(**kwargs)

    def __getitem__(self, index: int):
        return self._commands[index]

    def __setitem__(self, index: int, value: Union[MoveTo, LineTo, HorizontalLine, VerticalLine, CurveTo]):
        self._commands[index] = value

    def add(self, c: Union[MoveTo, LineTo, HorizontalLine, VerticalLine, CurveTo]):
        self._commands.append(c)

    def move_to(self, x: float, y: float):
        self.add(MoveTo(x, y))

    def move_relative(self, x: float, y: float):
        self.add(MoveTo(x, y, relative=True))

    def line_to(self, x: float, y: float):
        self.add(LineTo(x, y))

    def line_relative(self, x: float, y: float):
        self.add(LineTo(x, y, relative=True))

    def horizontal_line(self, x: float, y: float):
        self.add(HorizontalLine(x, y))

    def horizontal_line_relative(self, x: float, y: float):
        self.add(HorizontalLine(x, y, relative=True))

    def vertical_line(self, x: float, y: float):
        self.add(VerticalLine(x, y))

    def vertical_line_relative(self, x: float, y: float):
        self.add(VerticalLine(x, y, relative=True))

    def path_to(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        self.add(CurveTo(x1, y1, x2, y2, x3, y3))

    def create_element(self, root):
        element = ET.SubElement(root, 'path')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element):
        element.set('d', ''.join(['{}, '.format(str(c)) for c in self._commands]+' Z'))
        super(Path, self).set_element_attributes(element)



class MoveTo:
    def __init__(self, x: float, y: float, relative: bool = False):
        self._x = x
        self._y = y
        self._relative = bool

    def __str__(self):
        if self._relative:
            return 'm {} {}'.format(self._x,self._y)
        else:
            return 'M {} {}'.format(self._x,self._y)


class LineTo:
    def __init__(self, x: float, y: float, relative: bool = False):
        self._x = x
        self._y = y
        self._relative = bool

    def __str__(self):
        if self._relative:
            return 'l {} {}'.format(self._x,self._y)
        else:
            return 'L {} {}'.format(self._x,self._y)

class HorizontalLine:
    def __init__(self, x: float, relative: bool = False):
        self._x = x
        self._relative = bool

    def __str__(self):
        if self._relative:
            return 'h {}'.format(self._x)
        else:
            return 'H {}'.format(self._x)


class VerticalLine:
    def __init__(self, y: float, relative: bool = False):
        self._y = y
        self._relative = bool

    def __str__(self):
        if self._relative:
            return 'v {}'.format(self._y)
        else:
            return 'V {}'.format(self._y)


class CurveTo:
    def __init__(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3

    def __str__(self):
        return ' C {} {} {} {} {} {}'.format(self._x1, self._y1, self._x2, self._y2, self._x3, self._y3)
