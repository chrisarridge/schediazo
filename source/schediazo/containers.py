import xml.etree.ElementTree as ET
from typing import List, Union

import pint

from .attributes import Clip
from .part import PartDict
from .units import ureg

class Group(Clip,PartDict):
    """Grouped set of drawing elements
    """
    def __init__(self, **kwargs):
        """Initialise
        """
        super(Group,self).__init__(**kwargs)
        self._tag = 'g'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the group under.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.

        """
        super(Group, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



class ClipPath(PartDict):
    """Grouped set of drawing elements that are a path we can clip to
    """
    def __init__(self, **kwargs):
        """Initialise
        """
        super(ClipPath,self).__init__(**kwargs)
        self._tag = 'clipPath'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the clip path under.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.

        """
        super(ClipPath, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)



class Definitions(PartDict):
    """Set of definitions that can be used throughout a drawing.
    """
    def __init__(self):
        """Initialise
        """
        super(Definitions,self).__init__()
        self._tag = 'defs'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element],
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the defs tag under.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.

        """
        super(Definitions, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)
