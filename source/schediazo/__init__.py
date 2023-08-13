## ==========================================================================
##
## Module metadata.
##
## ==========================================================================
__author__ = "Chris Arridge"
__copyright__ = "Copyright 2018-2023 Chris Arridge"
__email__ = "chris@chrisarridge.co.uk"
__status__ = "development"
__docformat__ = "reStructuredText"
from ._version import __version__, __version_tuple__

from .paper import PaperSize
from .drawing import Drawing
from .units import ureg, Q_, cm, mm, inch, pt, pc, px, rad, deg
from .attributes import FontStyle, FontVariant, FontStretch, FontWeight, FontSize, TextAnchor

from .containers import Group, ClipPath
from .shapes import Line, Circle, Ellipse, Rect, Polyline, Polygon, EquilateralTriangle
from .text import Text, TextPath
from .image import Image
from .paths import Path, RawPath, MoveTo,MoveToDelta,LineTo,LineToDelta,PathLine,HlineTo,HlineToDelta,Hline,VlineTo,VlineToDelta,Vline,CubicBezierTo,CubicBezierToDelta,QuadraticBezierTo,QuadraticBezierToDelta

#from .transforms import Affine, identity
