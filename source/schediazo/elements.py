from typing import List, Union
from .transforms import Affine

class Element:
    """Base class for elements"""

    def __init__(self):
        self._children = []         # All child elements.

    def create_element(self, root):
        """Create the XML tree element for this drawing element"""
        pass

    def create_child_elements(self, root):
        """Create all the XML elements for the children of this element"""
        for child in self._children:
            child.create_element(root)






class AttributeMixinBase:
    """Base mixin for element attributes"""

    def set_element_attributes(self, element):
        """Set the attributes for this mixin"""
        pass




class Core(AttributeMixinBase):
    """Mixin to store attributes that are common to all elements"""
    def __init__(self, id: str = None, style: str = None, cssclass: str = None, **kwargs):
        self._id = id
        self._style = style
        self._cssclass = cssclass
        super(Core, self).__init__(**kwargs)

    def set_element_attributes(self, element):
        if self._id is not None:
            element.set('id', self._id)
        if self._style is not None:
            element.set('style', self._style)
        if self._cssclass is not None:
            element.set('class', self._cssclass)

class Transform(AttributeMixinBase):
    """Mixin to store transform attribute"""
    def __init__(self, transform: Affine=None, **kwargs):
        self._transform = transform
        super(Transform, self).__init__(**kwargs)

    def set_element_attributes(self, element):
        if self._transform is not None:
            element.set('transform', str(self._transform))

class Stroke(AttributeMixinBase):
    """Mixing to store stroke attributes"""
    def __init__(self, stroke: str = None,
                        stroke_dash_array: List[float] = None,
                        stroke_width: float = None, **kwargs):
        self._stroke = stroke
        self._stroke_dash_array = stroke_dash_array
        self._stroke_width = stroke_width
        super(Stroke, self).__init__(**kwargs)

    def set_element_attributes(self, element):
        if self._stroke is not None:
            element.set('stroke', self._stroke)
        if self._stroke_dash_array is not None:
            element.set('stroke-dash-array', ''.join(['{} '.format(x) for x in self._stroke_dash_array]))
        if self._stroke_width is not None:
            element.set('stroke-width', str(self._stroke_width))
        super(Stroke, self).set_element_attributes(element)



class Fill(AttributeMixinBase):
    """Mixing to store fill attributes"""

    def __init__(self, fill: str = None,
                        fill_opacity: float = None, **kwargs):
        self._fill = fill
        self._fill_opacity = fill_opacity
        super(Fill, self).__init__(**kwargs)

    def set_element_attributes(self, element):
        if self._fill is not None:
            element.set('fill', self._fill)
        if self._fill_opacity is not None:
            element.set('fill-opacity', self._fill_opacity)
        super(Fill, self).set_element_attributes(element)

class Clip(AttributeMixinBase):
    """Mixin to store clip path"""

    def __init__(self, clip_path: str=None, **kwargs):
        self._clip_path = clip_path
        super(Clip, self).__init__(**kwargs)

    def set_element_attributes(self, element):
        if self._clip_path is not None:
            element.set('clip-path', 'url(#'+self._clip_path+')')
        super(Clip, self).set_element_attributes(element)
