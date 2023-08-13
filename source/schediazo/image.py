import xml.etree.ElementTree as ET
import base64
import io
import uuid
from typing import List, Union

import PIL.Image
import pint

from .attributes import Transform, Styling, Clip
from .part import PartBase
from .units import _tostr, ureg


class Image(Transform,Clip,Styling,PartBase):
    """Embedded image
    """
    def __init__(self, x: pint.Quantity, y: pint.Quantity, width: pint.Quantity, height: pint.Quantity,
                        image: PIL.Image.Image=None, href: str=None,
                        preserve_aspect_ratio: bool=True, **kwargs):
        """Initialise

        Parameters
        ----------
        x : pint.Quantity
            Absolute x coordinate for the image location.
        y : pint.Quantity
            Absolute y coordinate for the image location.
        width : pint.Quantity
            Width of the image.
        height : pint.Quantity
            Height of the image.
        image : PIL.Image.Image, optional
            Image object, if there's no href then the image will be embedded as a base64 encoded png.
        href : str, optional
            If this is given then it takes priority over any PIL.Image.Image given.
        preserve_aspect_ratio : bool, optional
            Preserve the aspect ratio of the image, by default True

        Raises
        ------
        ValueError
            If there's no image or href.
        """
        if image is None and href is None:
             raise ValueError
        if image is not None and not isinstance(image,PIL.Image.Image):
            raise TypeError("image must be PIL.Image.Image object")
        self._image = image

        if href is not None and not isinstance(href,str):
            raise TypeError("href must be a string")
        self._href = href

        if not (isinstance(x, pint.Quantity) and isinstance(y, pint.Quantity)):
            raise TypeError("x and y coordinates must by pint.Quantity objects")
        self._x = x
        self._y = y

        if not (isinstance(width, pint.Quantity) and isinstance(height, pint.Quantity)):
            raise TypeError("width and height must by pint.Quantity objects")
        self._width = width
        self._height = height

        if not isinstance(preserve_aspect_ratio, bool):
            raise TypeError("preserve_aspect_ratio must be a boolean")
        self._preserve_aspect_ratio = preserve_aspect_ratio

        super(Image,self).__init__(**kwargs)
        self._tag = 'image'

    def set_element_attributes(self, element: Union[ET.Element,ET.SubElement], 
                               device_per_length: pint.Quantity=72*ureg.device/ureg.inch,
                               device_per_pixel: pint.Quantity=1*ureg.device/ureg.px):
        """Set SVG attributes for the image element.

        Parameters
        ----------
        element : Union[ET.Element,ET.SubElement]
            Element in which to set the 'x', 'w', 'width, 'height', 'preserveAspectRatio', 'href' and 'xlink:href' attributes.
        device_per_length : pint.Quantity, default 72 device units per inch
            A value to scale any coordinates in metres into device units (only used for some shapes, e.g., paths, PolyLines,
            where there the units are in pixels. (user coordinates).
        device_per_pixel : pint.Quantity, default 1 device units per pixel
            A value to scale any coordinates in pixels into device units.
        """
        element.set('x', _tostr(self._x))
        element.set('y', _tostr(self._y))
        element.set('width', _tostr(self._width))
        element.set('height', _tostr(self._height))
        element.set('preserveAspectRatio', str(self._preserve_aspect_ratio))

        if self._href is not None:
            element.set('href', self._href)
        else:
            buffer = io.BytesIO()
            self._image.save(buffer, format='png')
            encoded_data = 'data:image/png;base64,'+str(base64.b64encode(buffer.getbuffer()), encoding='ascii')
            element.set('xlink:href', encoded_data)
            element.set('href', encoded_data)

        super(Image, self).set_element_attributes(element, device_per_length=device_per_length, device_per_pixel=device_per_pixel)
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
            raise ValueError("No image to save")
