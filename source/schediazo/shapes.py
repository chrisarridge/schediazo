import xml.etree.ElementTree as ET
from typing import List, Union

import numpy as np
import pint

from .attributes import Styling, Stroke, Fill, Transform, Clip
from .part import PartBase
from .paths import *
from .units import _tostr, ureg, Q_, _scale

class Line(Stroke,Transform,Clip,Styling,PartBase):
    """Line
    """

    def __init__(self, x1: pint.Quantity, y1: pint.Quantity,
                 x2: pint.Quantity, y2: pint.Quantity,
                 **kwargs):
        """Initialise

        Parameters
        ----------
        x1 : pint.Quantity
            Start x coordinate for the line.
        y1 : pint.Quantity
            Start y coordinate for the line.
        x2 : pint.Quantity
            End x coordinate for the line.
        y2 : pint.Quantity
            End y coordinate for the line.
        """
        if not (isinstance(x1,pint.Quantity) and isinstance(x2,pint.Quantity)
                and isinstance(y1,pint.Quantity) and isinstance(y2,pint.Quantity)):
            raise TypeError
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
        return "Line(shape)({},{} to {},{})".format(_tostr(self._x1), _tostr(self._y1), _tostr(self._x2), _tostr(self._y2))

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the line element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'x1', 'y1', 'x2' and 'y2' attributes.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('x1', _tostr(self._x1))
        element.set('y1', _tostr(self._y1))
        element.set('x2', _tostr(self._x2))
        element.set('y2', _tostr(self._y2))
        super(Line, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

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

    def __init__(self, cx: pint.Quantity, cy: pint.Quantity, r: pint.Quantity, **kwargs):
        """Initialise

        Parameters
        ----------
        cx : pint.Quantity
            Absolute x coordinate of the centre of the circle.
        cy : pint.Quantity
            Absolute y coordinate of the centre of the circle.
        r : pint.Quantity
            Radius of the circle.
        """
        if not (isinstance(cx,pint.Quantity) and isinstance(cy,pint.Quantity)
                and isinstance(r,pint.Quantity)):
            raise TypeError
        self._cx = cx
        self._cy = cy
        self._r = r
        super(Circle,self).__init__(**kwargs)
        self._tag = 'circle'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the circle element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'cx', 'cy' and 'r' attributes.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('cx', _tostr(self._cx))
        element.set('cy', _tostr(self._cy))
        element.set('r', _tostr(self._r))
        super(Circle, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Circle(shape)(origin={},{} radius={})".format(_tostr(self._cx), _tostr(self._cy), _tostr(self._r))

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
    def __init__(self, cx: pint.Quantity, cy: pint.Quantity,
                        rx: pint.Quantity, ry: pint.Quantity, **kwargs):
        """Initialise

        Parameters
        ----------
        cx : pint.Quantity
            Absolute x coordinate of the centre of the ellipse.
        cy : pint.Quantity
            Absolute y coordinate of the centre of the ellipse.
        rx : pint.Quantity
            Radius of the ellipse in the x axis.
        ry : pint.Quantity
            Radius of the ellipse in the y axis.
        """
        if not (isinstance(cx,pint.Quantity) and isinstance(cy,pint.Quantity)
                and isinstance(rx,pint.Quantity) and isinstance(ry,pint.Quantity)):
            raise TypeError
        self._cx = cx
        self._cy = cy
        self._rx = rx
        self._ry = ry
        super(Ellipse,self).__init__(**kwargs)
        self._tag = 'ellipse'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the ellipse element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'cx', 'cy', 'rx' and 'ry' attributes.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('cx', _tostr(self._cx))
        element.set('cy', _tostr(self._cy))
        element.set('rx', _tostr(self._rx))
        element.set('ry', _tostr(self._ry))
        super(Ellipse, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Ellipse(shape)(origin={},{} radius={},{})".format(_tostr(self._cx), _tostr(self._cy), _tostr(self._rx), _tostr(self._ry))

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
    def __init__(self, x: pint.Quantity, y: pint.Quantity,
                        width: pint.Quantity, height: pint.Quantity,
                        rx: pint.Quantity=None, ry: pint.Quantity=None, **kwargs):
        """Initialise

        Parameters
        ----------
        x : pint.Quantity
            Absolute x position for the rectangle.
        y : pint.Quantity
            Absolute y position for the rectangle.
        width : pint.Quantity
            Width of the rectangle.
        height : pint.Quantity
            Height of the rectangle.
        rx : pint.Quantity
            Horizontal radius of the corner.
        ry : pint.Quantity
            Vertical radius of the corner.
        """
        if not (isinstance(x,pint.Quantity) and isinstance(y,pint.Quantity)
                and isinstance(width,pint.Quantity) and isinstance(height,pint.Quantity)):
            raise TypeError
        if rx is not None:
            if not isinstance(rx,pint.Quantity):
                raise TypeError
        if ry is not None:
            if not isinstance(ry,pint.Quantity):
                raise TypeError
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

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the rectangle element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'x', 'y', 'w' and 'h' attributes.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('x', _tostr(self._x))
        element.set('y', _tostr(self._y))
        element.set('width', _tostr(self._width))
        element.set('height', _tostr(self._height))
        if self._rx is not None:
            element.set('rx', _tostr(self._rx))
        if self._ry is not None:
            element.set('ry', _tostr(self._ry))
        super(Rect, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

    def __repr__(self) -> str:
        """Generate readable summary

        Returns
        -------
        str
        """
        return "Rect(shape)(origin={},{} width={} height={})".format(_tostr(self._x), _tostr(self._y), _tostr(self._width), _tostr(self._height))

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
    def __init__(self, x: Union[List[pint.Quantity],pint.Quantity], y: Union[List[pint.Quantity],pint.Quantity], **kwargs):
        """Initialise

        Parameters
        ----------
        x : Union[List[pint.Quantity],pint.Quantity]
            Absolute x coordinates for all the vertices along the polygon.
        y : Union[List[pint.Quantity],pint.Quantity]
            Absolute y coordinates for all the vertices along the polygon.
        """
        if not (isinstance(x,(list,pint.Quantity)) and isinstance(y,(list,pint.Quantity))):
            raise TypeError("x and y coordinates must be pint.Quantity objects")
        if isinstance(x,list):
            for coord in x:
                if not isinstance(coord,pint.Quantity):
                    raise TypeError("x and y coordinates must be pint.Quantity objects")
        if isinstance(y,list):
            for coord in y:
                if not isinstance(coord,pint.Quantity):
                    raise TypeError("x and y coordinates must be pint.Quantity objects")

        self._x = Q_.from_list(x)
        self._y = Q_.from_list(y)
        super(Polyline,self).__init__(**kwargs)
        self._tag = 'polyline'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the polyline element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'points' attribute.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('points', ''.join(['{},{} '.format(_scale(xi, device_per_length, device_per_pixel).magnitude,_scale(yi, device_per_length, device_per_pixel).magnitude) for xi,yi in zip(self._x,self._y)]))
        super(Polyline, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

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

    def __init__(self, x: Union[List[pint.Quantity],pint.Quantity], y: Union[List[pint.Quantity],pint.Quantity], **kwargs):
        """Initialise

        Parameters
        ----------
        x : Union[List[pint.Quantity],pint.Quantity]
            Absolute x coordinates for all the vertices along the polygon.
        y : Union[List[pint.Quantity],pint.Quantity]
            Absolute y coordinates for all the vertices along the polygon.
        """
        if not (isinstance(x,(list,pint.Quantity)) and isinstance(y,(list,pint.Quantity))):
            raise TypeError("x and y coordinates must be pint.Quantity objects")
        if isinstance(x,list):
            for coord in x:
                if not isinstance(coord,pint.Quantity):
                    raise TypeError("x and y coordinates must be pint.Quantity objects")
        if isinstance(y,list):
            for coord in y:
                if not isinstance(coord,pint.Quantity):
                    raise TypeError("x and y coordinates must be pint.Quantity objects")

        self._x = Q_.from_list(x)
        self._y = Q_.from_list(y)
        super(Polygon,self).__init__(**kwargs)
        self._tag = 'polygon'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the ellipse element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'points' attribute.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('points', ''.join(['{},{} '.format(_scale(xi, device_per_length, device_per_pixel).magnitude,_scale(yi, device_per_length, device_per_pixel).magnitude) for xi,yi in zip(self._x,self._y)]))
        super(Polygon, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

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
    def __init__(self, x0: pint.Quantity, y0: pint.Quantity, side: pint.Quantity, **kwargs):
        """Initialise

        Parameters
        ----------
        x0 : pint.Quantity
            Absolute x coordinate for the left-hand side of the triangle.
        y0 : pint.Quantity
            Absolute y coordinate for the centre of the triangle.
        side : pint.Quantity
            Length of each side of the equilateral triangle.
        """
        if not (isinstance(x0,pint.Quantity) and isinstance(y0,pint.Quantity)
                and isinstance(side,pint.Quantity)):
            raise TypeError("x0, y0 and side must all be pint.Quantity objects")
        self._x0 = x0
        self._y0 = y0
        self._side = side
        hh = 0.5*np.cos(np.radians(30))
        yorigin = 0.5*x0.units/np.cos(np.radians(30))
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
