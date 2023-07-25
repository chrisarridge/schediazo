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

from .drawing import Drawing
from .shapes import Line, Circle, Ellipse, Rect, Polyline, Polygon, EquilateralTriangle
from .text import Text, TextPath
from .image import Image
from .containers import Group, ClipPath
from .paths import Path, RawPath, MoveTo,MoveToDelta,LineTo,LineToDelta,PathLine,HlineTo,HlineToDelta,Hline,VlineTo,VlineToDelta,Vline,CubicBezierTo,CubicBezierToDelta,QuadraticBezierTo,QuadraticBezierToDelta
from .units import mm, cm, m, inch
from .transforms import Affine, identity
from .svg import Versions
from .attributes import FontStyle, FontVariant, FontStretch, FontWeight, FontSize, TextAnchor