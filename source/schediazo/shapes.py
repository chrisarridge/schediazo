import xml.etree.ElementTree as ET
from typing import List

import numpy as np

from .elements import Element, Core, Stroke, Fill, Transform, Clip



class Circle(Stroke,Fill,Transform,Clip,Core,Element):
    """Circle"""
    def __init__(self, cx: float, cy: float, r: float, **kwargs):
        self._cx = cx
        self._cy = cy
        self._r = r
        super(Circle,self).__init__(**kwargs)

    def create_element(self, root):
        element = ET.SubElement(root, 'circle')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element):
        element.set('cx', str(self._cx))
        element.set('cy', str(self._cy))
        element.set('r', str(self._r))
        super(Circle, self).set_element_attributes(element)



class Ellipse(Stroke,Fill,Transform,Clip,Core,Element):
    """Ellipse"""
    def __init__(self, cx: float, cy: float, rx: float, ry: float, **kwargs):
        self._cx = cx
        self._cy = cy
        self._rx = rx
        self._ry = ry
        super(Ellipse,self).__init__(**kwargs)

    def create_element(self, root):
        element = ET.SubElement(root, 'ellipse')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element):
        element.set('cx', str(self._cx))
        element.set('cy', str(self._cy))
        element.set('rx', str(self._rx))
        element.set('ry', str(self._ry))
        super(Ellipse, self).set_element_attributes(element)



class Rect(Stroke,Fill,Transform,Clip,Core,Element):
    """Rectangle"""
    def __init__(self, x: float, y: float, w: float, h: float, **kwargs):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        super(Rect,self).__init__(**kwargs)

    def create_element(self, root):
        element = ET.SubElement(root, 'rect')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element):
        element.set('x', str(self._x))
        element.set('y', str(self._y))
        element.set('w', str(self._w))
        element.set('h', str(self._h))
        super(Rect, self).set_element_attributes(element)



class Polyline(Stroke,Fill,Transform,Clip,Core,Element):
    """Polyline shape (open polygon)"""
    def __init__(self, x: List[float], y: List[float], **kwargs):
        self._x = np.array(x)
        self._y = np.array(y)
        super(Polyline,self).__init__(**kwargs)

    def create_element(self, root):
        element = ET.SubElement(root, 'polyline')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element):
        element.set('points', ''.join(['{},{} '.format(xi,yi) for xi,yi in zip(self._x,self._y)]))
        super(Polyline, self).set_element_attributes(element)



class Polygon(Stroke,Fill,Transform,Clip,Core,Element):
    """Polygon shape (closed polyline)"""
    def __init__(self, x: List[float], y: List[float], **kwargs):
        self._x = np.array(x)
        self._y = np.array(y)
        super(Polygon,self).__init__(**kwargs)

    def create_element(self, root):
        element = ET.SubElement(root, 'polygon')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element):
        element.set('points', ''.join(['{},{} '.format(xi,yi) for xi,yi in zip(self._x,self._y)]))
        super(Polygon, self).set_element_attributes(element)



class EquilateralTriangle(Polygon):
    """Equilateral triangle shape using a polygon (closed polyline)"""
    def __init__(self, x0: float, y0: float, side: float, **kwargs):
        self._x0 = x0
        self._y0 = y0
        self._side = side
        hh = 0.5*np.cos(np.radians(30))
        yorigin = 0.5/np.cos(np.radians(30))
        super(EquilateralTriangle, self).__init__(
                    [x0 + xp*side for xp in [0, 0.5, -0.5, 0]],
                    [-yorigin + y0 + yp*side for yp in [-hh, hh, hh, -hh]], **kwargs)

