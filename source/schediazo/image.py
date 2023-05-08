import xml.etree.ElementTree as ET
import base64
import io
import uuid
from typing import List, Union

import PIL.Image

from .attributes import Transform, Styling, Clip
from .part import PartBase



class Image(Transform,Clip,Styling,PartBase):
    """Embedded image
    """
    def __init__(self, x: float, y: float, width: float, height: float,
                        image: PIL.Image.Image=None, href: str=None,
                        preserveAspectRatio: bool=True, **kwargs):
        """Initialise

        Parameters
        ----------
        x : float
            Absolute x coordinate for the image location.
        y : float
            Absolute y coordinate for the image location.
        width : float
            Width of the image.
        height : float
            Height of the image.
        image : PIL.Image.Image, optional
            Image object, if there's no href then the image will be embedded as a base64 encoded png.
        href : str, optional
            If this is given then it takes priority over any PIL.Image.Image given.
        preserveAspectRatio : bool, optional
            Preserve the aspect ratio of the image, by default True

        Raises
        ------
        ValueError
            If there's no image or href.
        """
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
        self._tag = 'image'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement]):
        """Set SVG attributes for the image element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'x', 'w', 'width, 'height', 'preserveAspectRatio', 'href' and 'xlink:href' attributes.
        """
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
        """Saves the PIL.Image to a file and generates a url.

        Raises
        ------
        ValueError
            If the image isn't present.
        """
        if self._image is not None:
              self._href = str(uuid.uuid4())+'.png'
              self._image.save(self._href)
        else:
            raise ValueError

