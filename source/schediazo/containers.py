import xml.etree.ElementTree as ET
from typing import List, Union

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

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the group under.
        """
        super(Group, self).set_element_attributes(element)



class ClipPath(PartDict):
    """Grouped set of drawing elements that are a path we can clip to
    """
    def __init__(self, clip_path_units: str=None, **kwargs):
        """Initialise

        Parameters
        ----------
        clip_path_units : str, optional
            Units for the clip path.
        """
        self._clip_path_units = clip_path_units
        super(ClipPath,self).__init__(**kwargs)
        self._tag = 'clipPath'

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to create the clip path under.
        """
        if self._clip_path_units is not None:
            element.set('clipPathUnits', self._clip_path_units)
        super(ClipPath, self).set_element_attributes(element)
