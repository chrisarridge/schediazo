import xml.etree.ElementTree as ET
import base64
import io
import uuid
from typing import List

import PIL.Image

from .elements import Element, Transform, Core, Clip




class Image(Transform,Clip,Core,Element):
    """Embedded image"""
    def __init__(self, x: float, y: float, width: float, height: float, image: PIL.Image.Image=None, href: str=None, preserveAspectRatio: bool=True, **kwargs):
        if image is None and href is None:
             raise ValueError

        self._x = x
        self._y = y
        self._width = width
        self._height = height

        self._image = image
        self._href = href

        self._preserveAspectRatio = preserveAspectRatio
        super(Image,self).__init__(**kwargs)

    def create_element(self, root):
        element = ET.SubElement(root, 'image')
        self.set_element_attributes(element)
        return element

    def set_element_attributes(self, element):

        element.set('x', str(self._x))
        element.set('y', str(self._y))
        element.set('width', str(self._width))
        element.set('height', str(self._height))
        element.set('preserveAspectRatio', str(self._preserveAspectRatio))

        if self._href is not None:
            element.set('href', self._href)
        else:
            buffer = io.BytesIO()
            self._image.save(buffer, format='png')
            encoded_data = 'data:image/png;base64,'+str(base64.b64encode(buffer.getbuffer()), encoding='ascii')
            element.set('xlink:href', encoded_data)
            element.set('href', encoded_data)

        super(Image, self).set_element_attributes(element)
        return element


    def save_image_and_generate_href(self):
        if self._image is not None:
              self._href = str(uuid.uuid4())+'.png'
              self._image.save(self._href)
        else:
            raise ValueError

