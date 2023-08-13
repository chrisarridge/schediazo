import xml.etree.ElementTree as ET
from typing import Union, Iterable

import pint

from .attributes import Styling, Stroke, Fill, Transform, Clip
from .part import PartBase
from .units import _tostr, ureg, _scale



class MoveTo:
    """Moves the position in absolute coordinates
    """
    def __init__(self, x: pint.Quantity, y: pint.Quantity):
        """Initialise

        Parameters
        ----------
        x : pint.Quantity
            The new absolute x position.
        y : pint.Quantity
            The new absolute y position.
        """
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'Move({},{})'.format(_tostr(self._x),_tostr(self._y))

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        x = _scale(self._x, device_per_length, device_per_pixel)
        y = _scale(self._y, device_per_length, device_per_pixel)
        return 'M {} {}'.format(x.magnitude,y.magnitude)



class MoveToDelta:
    """Moves the position in relative coordinates
    """
    def __init__(self, dx: pint.Quantity, dy: pint.Quantity):
        """Initialise

        Parameters
        ----------
        dx : pint.Quantity
            The relative x shift.
        dy : pint.Quantity
            The relative y shift.
        """
        self._dx = dx
        self._dy = dy

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'MoveDelta({},{})'.format(self._dx,self._dy)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        dx = _scale(self._dx, device_per_length, device_per_pixel)
        dy = _scale(self._dy, device_per_length, device_per_pixel)
        return 'm {} {}'.format(dx.magnitude,dy.magnitude)



class LineTo:
    """Draws a line from the current position to an absolute position
    """
    def __init__(self, x: pint.Quantity, y: pint.Quantity):
        """Initialise

        Parameters
        ----------
        x : pint.Quantity
            The absolute x position of the end of the line.
        y : pint.Quantity
            The absolute y position of the end of the line.
        """
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'LineTo({},{})'.format(self._x,self._y)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        x = _scale(self._x, device_per_length, device_per_pixel)
        y = _scale(self._y, device_per_length, device_per_pixel)
        return 'L {} {}'.format(x.magnitude,y.magnitude)



class LineToDelta:
    """Draws a line from the current position to an relative position
    """
    def __init__(self, dx: pint.Quantity, dy: pint.Quantity):
        """Initialise

        Parameters
        ----------
        dx : pint.Quantity
            The relative x position of the end of the line.
        dy : pint.Quantity
            The relative y position of the end of the line.
        """
        self._dx = dx
        self._dy = dy

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'LineToDelta({},{})'.format(self._dx,self._dy)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        dx = _scale(self._dx, device_per_length, device_per_pixel)
        dy = _scale(self._dy, device_per_length, device_per_pixel)
        return 'l {} {}'.format(dx.magnitude,dy.magnitude)



class PathLine:
    """Draws a line from one position to another
    """
    def __init__(self, x0: pint.Quantity, y0: pint.Quantity, x1: pint.Quantity, y1: pint.Quantity):
        """Initialise

        Parameters
        ----------
        x0 : pint.Quantity
            The absolute x position of the start of the line.
        y0 : pint.Quantity
            The absolute y position of the start of the line.
        x1 : pint.Quantity
            The absolute x position of the end of the line.
        y1 : pint.Quantity
            The absolute y position of the end of the line.
        """
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'PathLine({},{} to {},{})'.format(self._x0,self._y0,self._x1,self._y1)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        x0 = _scale(self._x0, device_per_length, device_per_pixel)
        y0 = _scale(self._y0, device_per_length, device_per_pixel)
        x1 = _scale(self._x1, device_per_length, device_per_pixel)
        y1 = _scale(self._y1, device_per_length, device_per_pixel)
        return 'M {} {} L {} {}'.format(x0,y0,x1,y1)



class HlineTo:
    """Draws a horizontal line from the current position to an absolute position
    """
    def __init__(self, x: pint.Quantity):
        """Initialise

        Parameters
        ----------
        x : pint.Quantity
            The absolute x position of the end of the line.
        """
        self._x = x

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'HorizontalLineTo({})'.format(self._x)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        x = _scale(self._x, device_per_length, device_per_pixel)
        return 'H {}'.format(x.magnitude)



class HlineToDelta:
    """Draws a horizontal line from the current position to a relative position
    """
    def __init__(self, dx: pint.Quantity):
        """Initialise

        Parameters
        ----------
        dx : pint.Quantity
            The relative x position of the end of the line.
        """
        self._dx = dx

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'HorizontalLineToDelta({})'.format(self._dx)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        dx = _scale(self._dx, device_per_length, device_per_pixel)
        return 'h {} '.format(dx.magnitude)



class Hline:
    """Draws a horizontal line from one absolute position to another absolute position
    """
    def __init__(self, x0: pint.Quantity, y: pint.Quantity, x1: pint.Quantity):
        """Initialise

        Parameters
        ----------
        x0 : pint.Quantity
            The absolute x position of the start of the line.
        y : pint.Quantity
            The absolute y position of the line.
        x1 : pint.Quantity
            The absolute x position of the end of the line.
        """
        self._x0 = x0
        self._y = y
        self._x1 = x1

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'HorizontalLine({},{} to {},{})'.format(self._x0,self._y,self._x1,self._y)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        x0 = _scale(self._x0, device_per_length, device_per_pixel)
        y = _scale(self._y, device_per_length, device_per_pixel)
        x1 = _scale(self._x1, device_per_length, device_per_pixel)
        return 'M {} {} H {}'.format(x0.magnitude, y.magnitude, x1.magnitude)


class VlineTo:
    """Draws a vertical line from the current position to an absolute position
    """
    def __init__(self, y: pint.Quantity):
        """Initialise

        Parameters
        ----------
        y : pint.Quantity
            The absolute y position of the end of the line.
        """
        self._y = y

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'VerticalLineTo({})'.format(self._y)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        y = _scale(self._y, device_per_length, device_per_pixel)
        return 'V {}'.format(y.magnitude)



class VlineToDelta:
    """Draws a vertical line from the current position to a relative position
    """
    def __init__(self, dy: pint.Quantity):
        """Initialise

        Parameters
        ----------
        dy : pint.Quantity
            The relative y position of the end of the line.
        """
        self._dy = dy

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'VerticalLineToDelta({})'.format(self._dy)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        dy = _scale(self._dy, device_per_length, device_per_pixel)
        return 'v {}'.format(dy.magnitude)


class Vline:
    """Draws a vertical line from one absolute position to another absolute position
    """
    def __init__(self, x: pint.Quantity, y0: pint.Quantity, y1: pint.Quantity):
        """Initialise

        Parameters
        ----------
        x : pint.Quantity
            The absolute x position of the line.
        y0 : pint.Quantity
            The absolute y position of the start of the line.
        y1 : pint.Quantity
            The absolute y position of the end of the line.
        """
        self._x = x
        self._y0 = y0
        self._y1 = y1

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'VerticalLine({},{} to {},{})'.format(self._x,self._y0,self._x,self._y1)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        x = _scale(self._x, device_per_length, device_per_pixel)
        y0 = _scale(self._y0, device_per_length, device_per_pixel)
        y1 = _scale(self._y1, device_per_length, device_per_pixel)
        return 'M {} {} V {}'.format(x.magnitude, y0.magnitude, y1.magnitude)



class CubicBezierTo:
    """Draw a cubic Bezier from the current position to a set of absolute coordinates.
    """

    def __init__(self, xc1: pint.Quantity, yc1: pint.Quantity, xc2: pint.Quantity, yc2: pint.Quantity, x: pint.Quantity, y: pint.Quantity):
        """Initialise

        Parameters
        ----------
        xc1 : pint.Quantity
            Absolute x coordinate for the first control point.
        yc1 : pint.Quantity
            Absolute y coordinate for the first control point.
        xc2 : pint.Quantity
            Absolute x coordinate for the second control point.
        yc2 : pint.Quantity
            Absolute y coordinate for the second control point.
        x : pint.Quantity
            Absolute X coordinate for the end of the Bezier.
        y : pint.Quantity
            Absolute Y coordinate for the end of the Bezier.
        """
        self._xc1 = xc1
        self._yc1 = yc1
        self._xc2 = xc2
        self._yc2 = yc2
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'CubicBezier(c1: {},{}, c2: {},{} to {},{})'.format(self._xc1,self._yc1,self._xc2,self._yc2,self._x,self._y)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        xc1 = _scale(self._xc1, device_per_length, device_per_pixel)
        yc1 = _scale(self._yc1, device_per_length, device_per_pixel)
        xc2 = _scale(self._xc2, device_per_length, device_per_pixel)
        yc2 = _scale(self._yc2, device_per_length, device_per_pixel)
        x = _scale(self._x, device_per_length, device_per_pixel)
        y = _scale(self._y, device_per_length, device_per_pixel)
        return 'C {} {}, {} {}, {} {}'.format(xc1.magnitude,yc1.magnitude,xc2.magnitude,yc2.magnitude,x.magnitude,y.magnitude)



class CubicBezierToDelta:
    """Draw a cubic Bezier from the current position to a set of relative coordinates.
    """

    def __init__(self, dxc1: pint.Quantity, dyc1: pint.Quantity, dxc2: pint.Quantity, dyc2: pint.Quantity, dx: pint.Quantity, dy: pint.Quantity):
        """Initialise

        Parameters
        ----------
        dxc1 : pint.Quantity
            Relative x coordinate for the first control point.
        dyc1 : pint.Quantity
            Relative y coordinate for the first control point.
        dxc2 : pint.Quantity
            Relative x coordinate for the second control point.
        dyc2 : pint.Quantity
            Relative y coordinate for the second control point.
        dx : pint.Quantity
            Relative x coordinate for the end of the Bezier.
        dy : pint.Quantity
            Relative y coordinate for the end of the Bezier.
        """
        self._dxc1 = dxc1
        self._dyc1 = dyc1
        self._dxc2 = dxc2
        self._dyc2 = dyc2
        self._dx = dx
        self._dy = dy

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'CubicBezierDelta(c1: {},{}, c2: {},{} to {},{})'.format(self._dxc1,self._dyc1,self._dxc2,self._dyc2,self._dx,self._dy)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        dxc1 = _scale(self._dxc1, device_per_length, device_per_pixel)
        dyc1 = _scale(self._dyc1, device_per_length, device_per_pixel)
        dxc2 = _scale(self._dxc2, device_per_length, device_per_pixel)
        dyc2 = _scale(self._dyc2, device_per_length, device_per_pixel)
        dx = _scale(self._dx, device_per_length, device_per_pixel)
        dy = _scale(self._dy, device_per_length, device_per_pixel)
        return 'c {} {}, {} {}, {} {}'.format(dxc1.magnitude,dyc1.magnitude,dxc2.magnitude,dyc2.magnitude,dx.magnitude,dy.magnitude)



class QuadraticBezierTo:
    """Draw a quadratic Bezier from the current position to a set of absolute coordinates.
    """

    def __init__(self, xc: pint.Quantity, yc: pint.Quantity, x: pint.Quantity, y: pint.Quantity):
        """Initialise

        Parameters
        ----------
        xc : pint.Quantity
            Absolute x coordinate for the control point.
        yc : pint.Quantity
            Absolute y coordinate for the control point.
        x : pint.Quantity
            Absolute X coordinate for the end of the Bezier.
        y : pint.Quantity
            Absolute Y coordinate for the end of the Bezier.
        """
        self._xc = xc
        self._yc = yc
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'QuadraticBezier(c: {},{} to {},{})'.format(self._xc,self._yc,self._x,self._y)

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        xc = _scale(self._xc, device_per_length, device_per_pixel)
        yc = _scale(self._yc, device_per_length, device_per_pixel)
        x = _scale(self._x, device_per_length, device_per_pixel)
        y = _scale(self._y, device_per_length, device_per_pixel)
        return 'Q {} {}, {} {}'.format(xc.magnitude,yc.magnitude,x.magnitude,y.magnitude)



class QuadraticBezierToDelta:
    """Draw a quadratic Bezier from the current position to a set of relative coordinates.
    """

    def __init__(self, dxc: pint.Quantity, dyc: pint.Quantity, dx: pint.Quantity, dy: pint.Quantity):
        """Initialise

        Parameters
        ----------
        dxc : pint.Quantity
            Relative x coordinate for the control point.
        dyc : pint.Quantity
            Relative y coordinate for the control point.
        dx : pint.Quantity
            Relative x coordinate for the end of the Bezier.
        dy : pint.Quantity
            Relative y coordinate for the end of the Bezier.
        """
        self._dxc = dxc
        self._dyc = dyc
        self._dx = dx
        self._dy = dy

    def __repr__(self) -> str:
        """Return a string representation

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'QuadraticBezierDelta(c: {},{} to {},{})'.format(self._dxc,self._dyc,self._dx,self._dy)


    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert command into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        dxc = _scale(self._dxc, device_per_length, device_per_pixel)
        dyc = _scale(self._dyc, device_per_length, device_per_pixel)
        dx = _scale(self._dx, device_per_length, device_per_pixel)
        dy = _scale(self._dy, device_per_length, device_per_pixel)
        return 'q {} {}, {} {}'.format(dxc.magnitude,dyc.magnitude,dx.magnitude,dy.magnitude)


_COMMAND_CLASSES = (MoveTo,MoveToDelta,LineTo,LineToDelta,PathLine,
                    HlineTo,HlineToDelta,Hline,VlineTo,VlineToDelta,Vline,
                    CubicBezierTo,CubicBezierToDelta,QuadraticBezierTo,QuadraticBezierToDelta)
_COMMAND_UNION = Union[MoveTo,MoveToDelta,LineTo,LineToDelta,PathLine,
                    HlineTo,HlineToDelta,Hline,VlineTo,VlineToDelta,Vline,
                    CubicBezierTo,CubicBezierToDelta,QuadraticBezierTo,QuadraticBezierToDelta]


class RawPath(list):
    """Path that can be used in a part or as a path for text.
    """

    def __init__(self, items: Iterable, closed: bool = False):
        """Initialise

        Parameters
        ----------
        items : Iterable
            Either another RawPath or some other iterable containing a set of drawing command objects.
        closed : bool, optional
            Whether the path is closed or not.

        Raises
        ------
        ValueError
            Exception if any item in the iterable is not a drawing command.
        """
        for item in items:
            if not isinstance(item, _COMMAND_CLASSES):
                raise ValueError
        super().__init__(items)
        self._closed = closed

    def __setitem__(self, index: int, item: _COMMAND_UNION):
        """Set a specific index to a new drawing command.

        Parameters
        ----------
        index : int
            Index to change.
        item : _COMMAND_UNION
            The new drawing command.

        Raises
        ------
        ValueError
            Exception if the new item is not a drawing command.
        """
        if not isinstance(item, _COMMAND_CLASSES):
            raise ValueError
        super().__setitem__(index, item)

    def insert(self, index: int, item: _COMMAND_UNION):
        """Insert a new drawing command at the given index.

        Parameters
        ----------
        index : int
            Index to insert the command
        item : _COMMAND_UNION
            The new drawing command.

        Raises
        ------
        ValueError
            Exception if the new item is not a drawing command.
        """
        if not isinstance(item, _COMMAND_CLASSES):
            raise ValueError
        super().insert(index, item)

    def append(self, item: _COMMAND_UNION):
        """Append a new drawing command to the end of the path.

        Parameters
        ----------
        item : _COMMAND_UNION
            The new drawing command.

        Raises
        ------
        ValueError
            Exception if the new item is not a drawing command.
        """
        if not isinstance(item, _COMMAND_CLASSES):
            raise ValueError
        super().append(item)

    def extend(self, other: Iterable):
        """Extend this path with a set of drawing commands.

        Parameters
        ----------
        other : Iterable
            Either another RawPath or some other iterable containing a set of drawing command objects.

        Raises
        ------
        ValueError
            Exception if any item in the iterable is not a drawing command.
        """
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            for item in other:
                if not isinstance(item, _COMMAND_CLASSES):
                    raise ValueError
            super().extend(other)

    def close(self):
        """Set the path to be closed.
        """
        self._closed = True

    def to_svg(self, device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                    device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Convert path into an SVG string

        Parameters
        ----------
        device_per_length : pint.Quantity, optional
            Device units per unit length, by default 72*ureg.device/ureg.inch
        device_per_pixel : pint.Quantity, optional
            Device units per pixel, by default 1*ureg.device/ureg.px
        """
        tmp = ' '.join(c.to_svg(device_per_length,device_per_pixel) for c in self.__iter__())

        if self._closed:
            tmp += ' Z'

        return tmp



class Path(Stroke,Fill,Transform,Clip,Styling,PartBase):
    """Path shape
    """
    def __init__(self, path: RawPath, **kwargs):
        """Initialise

        Parameters
        ----------
        path : RawPath
            The path that will be made into the path part.
        """
        if not isinstance(path, RawPath):
            raise TypeError("path should be a RawPath object")
        self._path = path

        super(Path,self).__init__(**kwargs)
        self._tag = 'path'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the attributes in the XML tree element

        Sets the "d" attribute.

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
        element.set('d', self._path.to_svg(device_per_length, device_per_pixel))
        super(Path, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)

