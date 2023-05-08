## ==========================================================================
##
## Module metadata.
##
## ==========================================================================
__author__ = "Chris Arridge"
__copyright__ = "Copyright 2018-2023 Chris Arridge"
__version__ = "0.2.0"
__email__ = "chris@chrisarridge.co.uk"
__status__ = "development"
__date__ = " 08 May 2023"
__docformat__ = "reStructuredText"


from .drawing import Drawing
from .shapes import Line, Circle, Ellipse, Rect, Polyline, Polygon, EquilateralTriangle
from .image import Image
from .containers import Group, ClipPath
from .paths import Path, RawPath
from .units import mm, cm, m, inch
from .transforms import Affine, identity
from .svg import Versions