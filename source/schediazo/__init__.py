## ==========================================================================
##
## Module metadata.
##
## ==========================================================================
__author__ = "Chris Arridge"
__copyright__ = "Copyright 2018-2023 Chris Arridge"
__version__ = "0.1.0"
__email__ = "chris@chrisarridge.co.uk"
__status__ = "development"
__date__ = " 29 April 2023"
__docformat__ = "reStructuredText"


from .units import mm, cm, m, inch
from .core import Versions, Drawing
from .shapes import Circle, Ellipse, Rect, Polyline, Polygon, EquilateralTriangle
from .transforms import Affine, identity
from .image import Image
from .containers import Group, ClipPath
