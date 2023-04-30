import xml.etree.ElementTree as ET
from typing import List, Union

from .elements import Element, Core, Clip

class Group(Clip,Core,Element):
    """Grouped set of drawing elements"""
    def __init__(self, **kwargs):
        super(Group,self).__init__(**kwargs)
        
    def create_element(self, root: ET.SubElement):
        """Create the element and set the attributes
        
        Args:
            :param xml.etree.ElementTree.SubElement root: Element to create this group within.
        """
        element = ET.SubElement(root, 'g')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Create the element and set the attributes
        
        Args:
            :param SubElement | Element element: Element to set the attributes in.
        """
        super(Group, self).set_element_attributes(element)



class ClipPath(Core,Element):
    """Grouped set of drawing elements that are a path we can clip to"""
    def __init__(self, clip_path_units: str=None, **kwargs):
        self._clip_path_units = clip_path_units
        super(ClipPath,self).__init__(**kwargs)

    def create_element(self, root):
        """Create the element and set the attributes
        
        Args:
            :param xml.etree.ElementTree.SubElement root: Element to create this group within.
        """
        element = ET.SubElement(root, 'clipPath')
        self.set_element_attributes(element)
        self.create_child_elements(element)
        return element

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Create the element and set the attributes
        
        Args:
            :param SubElement | Element element: Element to set the attributes in.
        """
        if self._clip_path_units is not None:
            element.set('clipPathUnits', self._clip_path_units)
        super(ClipPath, self).set_element_attributes(element)
