import xml.etree.ElementTree as ET
from typing import List, Union

import pint

from .attributes import Clip
from .part import PartDict

class Group(Clip,PartDict):
    """Grouped set of drawing elements
    """
    def __init__(self, **kwargs):
        """Initialise
        """
        super(Group,self).__init__(**kwargs)
        self._tag = 'g'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element], dpi: pint.Quantity=None):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the group under.
        dpi : pint.Quantity, default None
            A value to scale any coordinates in metres into pixels (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).  The default is 1:1.

        """
        super(Group, self).set_element_attributes(element, dpi=dpi)



class ClipPath(PartDict):
    """Grouped set of drawing elements that are a path we can clip to
    """
    def __init__(self, **kwargs):
        """Initialise
        """
        self._clip_path_units = clip_path_units
        super(ClipPath,self).__init__(**kwargs)
        self._tag = 'clipPath'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element], dpi: pint.Quantity=None):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the clip path under.
        dpi : pint.Quantity, default None
            A value to scale any coordinates in metres into pixels (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).  The default is 1:1.

        """
        super(ClipPath, self).set_element_attributes(element, dpi=dpi)



class Definitions(PartDict):
    """Set of definitions that can be used throughout a drawing.
    """
    def __init__(self):
        """Initialise
        """
        super(Definitions,self).__init__()
        self._tag = 'defs'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element], dpi: pint.Quantity=None):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the defs tag under.
        dpi : pint.Quantity, default None
            A value to scale any coordinates in metres into pixels (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).  The default is 1:1.

        """
        super(Definitions, self).set_element_attributes(element, dpi=dpi)
