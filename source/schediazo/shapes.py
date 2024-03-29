import xml.etree.ElementTree as ET
from typing import List, Union

import numpy as np

from .attributes import Styling, Stroke, Fill, Transform, Clip
from .part import PartBase
from .paths import *

class Line(Stroke,Transform,Clip,Styling,PartBase):
    """Line
    """

    def __init__(self, x1: float, y1: float, x2: float, y2: float, **kwargs):
        """Initialise

        Parameters
        ----------
        x1 : float
            Start x coordinate for the line.
        y1 : float
            Start y coordinate for the line.
        x2 : float
            End x coordinate for the line.
        y2 : float
            End y coordinate for the line.
        """
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        super(Line,self).__init__(**kwargs)
        self._tag = 'line'

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Line(shape)({},{} to {},{})".format(self._x1, self._y1, self._x2, self._y2)

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the line element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'x1', 'y1', 'x2' and 'y2' attributes.
        """
        element.set('x1', str(self._x1))
        element.set('y1', str(self._y1))
        element.set('x2', str(self._x2))
        element.set('y2', str(self._y2))
        super(Line, self).set_element_attributes(element)

    def to_path(self) -> RawPath:
        """Convert shape into a path object.

        Returns
        -------
        RawPath
            Path representing the shape.
        """
        return RawPath([MoveTo(self._x1, self._y1), LineTo(self._x2, self._y2)])



class Circle(Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Circle part
    """

    def __init__(self, cx: float, cy: float, r: float, **kwargs):
        """Initialise

        Parameters
        ----------
        cx : float
            Absolute x coordinate of the centre of the circle.
        cy : float
            Absolute y coordinate of the centre of the circle.
        r : float
            Radius of the circle.
        """
        self._cx = cx
        self._cy = cy
        self._r = r
        super(Circle,self).__init__(**kwargs)
        self._tag = 'circle'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the circle element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'cx', 'cy' and 'r' attributes.
        """
        element.set('cx', str(self._cx))
        element.set('cy', str(self._cy))
        element.set('r', str(self._r))
        super(Circle, self).set_element_attributes(element)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Circle(shape)(origin={},{} radius={})".format(self._cx, self._cy, self._r)

    def to_path(self) -> RawPath:
        """Convert shape into a path object.

        Returns
        -------
        RawPath
            Path representing the shape.
        """
        th = np.linspace(0, 2*np.pi, 32)
        p = RawPath([MoveTo(self._cx + self._r*np.cos(th[0]), self._cy + self._r*np.sin(th[0]))], closed=True)
        [p.append(LineTo(self._cx + self._r*np.cos(th[i]), self._cy + self._r*np.sin(th[i]))) for i in range(1,len(th))]
        return p


class Ellipse(Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Ellipse part
    """
    def __init__(self, cx: float, cy: float, rx: float, ry: float, **kwargs):
        """Initialise

        Parameters
        ----------
        cx : float
            Absolute x coordinate of the centre of the ellipse.
        cy : float
            Absolute y coordinate of the centre of the ellipse.
        rx : float
            Radius of the ellipse in the x axis.
            _description_
        ry : float
            Radius of the ellipse in the y axis.
        """
        self._cx = cx
        self._cy = cy
        self._rx = rx
        self._ry = ry
        super(Ellipse,self).__init__(**kwargs)
        self._tag = 'ellipse'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the ellipse element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'cx', 'cy', 'rx' and 'ry' attributes.
        """
        element.set('cx', str(self._cx))
        element.set('cy', str(self._cy))
        element.set('rx', str(self._rx))
        element.set('ry', str(self._ry))
        super(Ellipse, self).set_element_attributes(element)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Ellipse(shape)(origin={},{} radius={},{})".format(self._cx, self._cy, self._rx, self._ry)

    def to_path(self) -> RawPath:
        """Convert shape into a path object.

        Returns
        -------
        RawPath
            Path representing the shape.
        """
        th = np.linspace(0, 2*np.pi, 32)
        p = RawPath([MoveTo(self._cx + self._rx*np.cos(th[0]), self._cy + self._ry*np.sin(th[0]))], closed=True)
        [p.append(LineTo(self._cx + self._rx*np.cos(th[i]), self._cy + self._ry*np.sin(th[i]))) for i in range(1,len(th))]
        return p


class Rect(Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Rectangle"""
    def __init__(self, x: float, y: float, width: float, height: float, rx: float=None, ry: float=None, **kwargs):
        """Initialise

        Parameters
        ----------
        x : float
            Absolute x position for the rectangle.
        y : float
            Absolute y position for the rectangle.
        width : float
            Width of the rectangle.
        height : float
            Height of the rectangle.
        rx : float
            Horizontal radius of the corner.
        ry : float
            Vertical radius of the corner.
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._rx = rx
        self._ry = ry
        if self._rx is None and self._ry is not None:
            self._rx = self._ry
        if self._rx is not None and self._ry is None:
            self._ry = self._rx
        super(Rect,self).__init__(**kwargs)
        self._tag = 'rect'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the rectangle element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'x', 'y', 'w' and 'h' attributes.
        """
        element.set('x', str(self._x))
        element.set('y', str(self._y))
        element.set('width', str(self._width))
        element.set('height', str(self._height))
        if self._rx is not None:
            element.set('rx', str(self._rx))
        if self._ry is not None:
            element.set('ry', str(self._ry))
        super(Rect, self).set_element_attributes(element)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Rect(shape)(origin={},{} width={} height={})".format(self._x, self._y, self._width, self._height)

    def to_path(self) -> RawPath:
        """Convert shape into a path object.

        Returns
        -------
        RawPath
            Path representing the shape.
        """
        if self._rx is None and self._ry is None:
            return RawPath([MoveTo(self._x,self._y),HlineToDelta(self._width),VlineToDelta(self._height),HlineToDelta(-self._width),VlineToDelta(-self._height)], closed=True)

        else:

            # Start at the point just after (in x) the rounded corner at the top-left.
            # ╭──────╮
            # │      │  
            # ╰──────╯
            p = RawPath([MoveTo(self._x+self._rx, self._y)], closed=True)

            # Draw the straight top edge.
            p.append(HlineToDelta(self._width-2*self._rx))

            # Draw the rounded corner.
            th = np.linspace(-0.5*np.pi, 0.0, 8)
            cx = self._x+self._width-self._rx
            cy = self._y+self._ry
            print(cx, self._rx)
            [p.append(LineTo(cx + self._rx*np.cos(th[i]), cy + self._ry*np.sin(th[i]))) for i in range(1,len(th))]

            # Draw the vertical right-hand line.
            p.append(VlineToDelta(self._height-2*self._ry))

            # Draw the rounded (bottom-right) corner.
            th = np.linspace(0.0, 0.5*np.pi, 8)
            cx = self._x+self._width-self._rx
            cy = self._y+self._height-self._ry
            [p.append(LineTo(cx + self._rx*np.cos(th[i]), cy + self._ry*np.sin(th[i]))) for i in range(1,len(th))]

            # Draw the bottom line.
            p.append(HlineToDelta(-(self._width-2*self._rx)))

            # Draw the bottom-right corner.
            th = np.linspace(0.5*np.pi, np.pi, 8)
            cx = self._x+self._rx
            cy = self._y+self._height-self._ry
            [p.append(LineTo(cx + self._rx*np.cos(th[i]), cy + self._ry*np.sin(th[i]))) for i in range(1,len(th))]

            # Draw the left-hand vertical line.
            p.append(VlineToDelta(-(self._height-2*self._ry)))

            # Draw the top-left corner.
            th = np.linspace(-np.pi, -0.5*np.pi, 8)
            cx = self._x+self._rx
            cy = self._y+self._ry
            [p.append(LineTo(cx + self._rx*np.cos(th[i]), cy + self._ry*np.sin(th[i]))) for i in range(1,len(th))]

            return p


class Polyline(Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Polyline shape (open polygon)
    """
    def __init__(self, x: Union[List[float],np.ndarray], y: Union[List[float],np.ndarray], **kwargs):
        """Initialise

        Parameters
        ----------
        x : Union[List[float],np.ndarray]
            Absolute x coordinates for all the vertices along the polyline.
        y : Union[List[float],np.ndarray]
            Absolute y coordinates for all the vertices along the polyline.
        """
        self._x = np.array(x)
        self._y = np.array(y)
        super(Polyline,self).__init__(**kwargs)
        self._tag = 'polyline'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the polyline element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'points' attribute.
        """
        element.set('points', ''.join(['{},{} '.format(xi,yi) for xi,yi in zip(self._x,self._y)]))
        super(Polyline, self).set_element_attributes(element)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Polyline(shape)(with {} points)".format(len(self._x))

    def to_path(self) -> RawPath:
        """Convert shape into a path object.

        Returns
        -------
        RawPath
            Path representing the shape.
        """
        return RawPath([MoveTo(self._x[0], self._y[0])]+[LineTo(x, y) for x,y in zip(self._x[1:],self._y[1:])])



class Polygon(Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Polygon shape (closed polyline)
    """

    def __init__(self, x: Union[List[float],np.ndarray], y: Union[List[float],np.ndarray], **kwargs):
        """Initialise

        Parameters
        ----------
        x : Union[List[float],np.ndarray]
            Absolute x coordinates for all the vertices along the polygon.
        y : Union[List[float],np.ndarray]
            Absolute y coordinates for all the vertices along the polygon.
        """
        self._x = np.array(x)
        self._y = np.array(y)
        super(Polygon,self).__init__(**kwargs)
        self._tag = 'polygon'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the ellipse element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'points' attribute.
        """
        element.set('points', ''.join(['{},{} '.format(xi,yi) for xi,yi in zip(self._x,self._y)]))
        super(Polygon, self).set_element_attributes(element)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Polygon(shape)(with {} points)".format(len(self._x))

    def to_path(self) -> RawPath:
        """Convert shape into a path object.

        Returns
        -------
        RawPath
            Path representing the shape.
        """
        return RawPath([MoveTo(self._x[0], self._y[0])]+[LineTo(x, y) for x,y in zip(self._x[1:],self._y[1:])]+[LineTo(self._x[0], self._y[0])], closed=True)



class EquilateralTriangle(Polygon):
    """Equilateral triangle shape using a polygon (closed polyline)
    """
    def __init__(self, x0: float, y0: float, side: float, **kwargs):
        """Initialise

        Parameters
        ----------
        x0 : float
            Absolute x coordinate for the left-hand side of the triangle.
        y0 : float
            Absolute y coordinate for the centre of the triangle.
        side : float
            Length of each side of the equilateral triangle.
        """
        self._x0 = x0
        self._y0 = y0
        self._side = side
        hh = 0.5*np.cos(np.radians(30))
        yorigin = 0.5/np.cos(np.radians(30))
        super(EquilateralTriangle, self).__init__(
                    [x0 + xp*side for xp in [0, 0.5, -0.5, 0]],
                    [-yorigin + y0 + yp*side for yp in [-hh, hh, hh, -hh]], **kwargs)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "EquilateralTriangle(shape)(with position {},{} and side={})".format(len(self._x0, self._y0, self._side))
