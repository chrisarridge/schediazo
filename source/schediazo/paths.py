import xml.etree.ElementTree as ET
from typing import Union, Iterable

from .attributes import Styling, Stroke, Fill, Transform, Clip
from .part import PartBase


class MoveTo:
    """Moves the position in absolute coordinates
    """
    def __init__(self, x: float, y: float):
        """Initialise

        Parameters
        ----------
        x : float
            The new absolute x position.
        y : float
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
        return 'Move({},{})'.format(self._x,self._y)

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'M {} {}'.format(self._x,self._y)



class MoveToDelta:
    """Moves the position in relative coordinates
    """
    def __init__(self, dx: float, dy: float):
        """Initialise

        Parameters
        ----------
        dx : float
            The relative x shift.
        dy : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'm {} {}'.format(self._dx,self._dy)



class LineTo:
    """Draws a line from the current position to an absolute position
    """
    def __init__(self, x: float, y: float):
        """Initialise

        Parameters
        ----------
        x : float
            The absolute x position of the end of the line.
        y : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'L {} {}'.format(self._x,self._y)



class LineToDelta:
    """Draws a line from the current position to an relative position
    """
    def __init__(self, dx: float, dy: float):
        """Initialise

        Parameters
        ----------
        dx : float
            The relative x position of the end of the line.
        dy : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'l {} {}'.format(self._dx,self._dy)



class PathLine:
    """Draws a line from one position to another
    """
    def __init__(self, x0: float, y0: float, x1: float, y1: float):
        """Initialise

        Parameters
        ----------
        x0 : float
            The absolute x position of the start of the line.
        y0 : float
            The absolute y position of the start of the line.
        x1 : float
            The absolute x position of the end of the line.
        y1 : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing commands

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'M {} {} L {} {}'.format(self._x0,self._y0,self._x1,self._y1)



class HlineTo:
    """Draws a horizontal line from the current position to an absolute position
    """
    def __init__(self, x: float):
        """Initialise

        Parameters
        ----------
        x : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'H {}'.format(self._x)



class HlineToDelta:
    """Draws a horizontal line from the current position to a relative position
    """
    def __init__(self, dx: float):
        """Initialise

        Parameters
        ----------
        dx : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'h {}'.format(self._dx)


class Hline:
    """Draws a horizontal line from one absolute position to another absolute position
    """
    def __init__(self, x0: float, y: float, x1: float):
        """Initialise

        Parameters
        ----------
        x0 : float
            The absolute x position of the start of the line.
        y : float
            The absolute y position of the line.
        x1 : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'M {} {} H {}'.format(self._x0,self._y, self._x1)



class VlineTo:
    """Draws a vertical line from the current position to an absolute position
    """
    def __init__(self, y: float):
        """Initialise

        Parameters
        ----------
        y : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'V {}'.format(self._y)



class VlineToDelta:
    """Draws a vertical line from the current position to a relative position
    """
    def __init__(self, dy: float):
        """Initialise

        Parameters
        ----------
        dy : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'v {}'.format(self._dy)


class Vline:
    """Draws a vertical line from one absolute position to another absolute position
    """
    def __init__(self, x: float, y0: float, y1: float):
        """Initialise

        Parameters
        ----------
        x : float
            The absolute x position of the line.
        y0 : float
            The absolute y position of the start of the line.
        y1 : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'M {} {} V {}'.format(self._x,self._y0, self._y1)



class CubicBezierTo:
    """Draw a cubic Bezier from the current position to a set of absolute coordinates.
    """

    def __init__(self, xc1: float, yc1: float, xc2: float, yc2: float, x: float, y: float):
        """Initialise

        Parameters
        ----------
        xc1 : float
            Absolute x coordinate for the first control point.
        yc1 : float
            Absolute y coordinate for the first control point.
        xc2 : float
            Absolute x coordinate for the second control point.
        yc2 : float
            Absolute y coordinate for the second control point.
        x : float
            Absolute X coordinate for the end of the Bezier.
        y : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'C {} {}, {} {}, {} {}'.format(self._xc1,self._yc1,self._xc2,self._yc2,self._x,self._y)



class CubicBezierToDelta:
    """Draw a cubic Bezier from the current position to a set of relative coordinates.
    """

    def __init__(self, dxc1: float, dyc1: float, dxc2: float, dyc2: float, dx: float, dy: float):
        """Initialise

        Parameters
        ----------
        dxc1 : float
            Relative x coordinate for the first control point.
        dyc1 : float
            Relative y coordinate for the first control point.
        dxc2 : float
            Relative x coordinate for the second control point.
        dyc2 : float
            Relative y coordinate for the second control point.
        dx : float
            Relative x coordinate for the end of the Bezier.
        dy : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'c {} {}, {} {}, {} {}'.format(self._dxc1,self._dyc1,self._dxc2,self._dyc2,self._dx,self._dy)



class QuadraticBezierTo:
    """Draw a quadratic Bezier from the current position to a set of absolute coordinates.
    """

    def __init__(self, xc: float, yc: float, x: float, y: float):
        """Initialise

        Parameters
        ----------
        xc : float
            Absolute x coordinate for the control point.
        yc : float
            Absolute y coordinate for the control point.
        x : float
            Absolute X coordinate for the end of the Bezier.
        y : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'Q {} {}, {} {}'.format(self._xc,self._yc,self._x,self._y)



class QuadraticBezierToDelta:
    """Draw a quadratic Bezier from the current position to a set of relative coordinates.
    """

    def __init__(self, dxc: float, dyc: float, dx: float, dy: float):
        """Initialise

        Parameters
        ----------
        dxc : float
            Relative x coordinate for the control point.
        dyc : float
            Relative y coordinate for the control point.
        dx : float
            Relative x coordinate for the end of the Bezier.
        dy : float
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

    def __str__(self) -> str:
        """Return the SVG path drawing command

        Returns
        -------
        str
            String representation of drawing command.
        """
        return 'q {} {}, {} {}'.format(self._dxc,self._dyc,self._dx,self._dy)


_COMMAND_CLASSES = (MoveTo,MoveToDelta,LineTo,LineToDelta,Line,
                    HlineTo,HlineToDelta,Hline,VlineTo,VlineToDelta,Vline,
                    CubicBezierTo,CubicBezierToDelta,QuadraticBezierTo,QuadraticBezierToDelta)
_COMMAND_UNION = Union[MoveTo,MoveToDelta,LineTo,LineToDelta,Line,
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

    def __str__(self) -> str:
        """Generate a string representation of the path for SVG.

        Returns
        -------
        str
            Set of SVG Path commands.
        """
        tmp = ' '.join(str(c) for c in self.__iter__())
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
        self._path = path
        super(Path,self).__init__(**kwargs)
        self._tag = 'path'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set the attributes in the XML tree element

        Sets the "d" attribute.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            The XML tree element that this method adds the attributes to.
        """
        element.set('d', str(self._path))
        super(Path, self).set_element_attributes(element)

