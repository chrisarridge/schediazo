"""Transformation classes and functions
"""
from typing import List, Tuple, Union
import math
import numpy as np

import pint

from .units import ureg, _tostr, Q_


class Affine:
    """Affine (scaling/translation) transforms from (u,v) to (p,q)"""
    def __init__(self):
        self._matrix = None
        self._operations = []
        self._units = None

    def __getitem__(self, index: int):
        """Directly get elements of the transformation matrix"""
        if self._matrix is None:
            self.build_matrix()
        return self._matrix[index]

    def __setitem__(self, index: int, value: float):
        """Directly set elements of the transformation matrix"""
        if self._matrix is None:
            self.build_matrix()
        self._matrix[index] = value

    def __str__(self):
        """Return an SVG-formatted string of transforms"""
        return ''.join([str(op)+' ' for op in self._operations])

    def __call__(self, u: Union[pint.Quantity,List[pint.Quantity],Tuple[pint.Quantity]],
                        v: Union[pint.Quantity,List[pint.Quantity],Tuple[pint.Quantity]]):
        return self.transform(u, v)

    def transform(self, u: Union[pint.Quantity,List[pint.Quantity],Tuple[pint.Quantity]],
                        v: Union[pint.Quantity,List[pint.Quantity],Tuple[pint.Quantity]]):
        """Transform some points given by u and v coordinates"""

        if self._matrix is None:
            self.build_matrix()

        if isinstance(u,pint.Quantity) and isinstance(v,pint.Quantity):

            # Check the units match those in the transform.
            if self._units is not None:
                if not (u.check(self._units) and v.check(self._units)):
                    raise ValueError("position units do not have the same units as those in the transform")

            if u.ndim==0 and v.ndim==0:
                if self._units is not None:
                    if not (u.check(self._units) and v.check(self._units)):
                        raise ValueError("position units do not have the same units as those in the transform")
                    p, q, _ = np.matmul(self._matrix, [u.to(self._units).magnitude, v.to(self._units).magnitude, 1.0])
                    return p*self._units, q*self._units
                else:
                    p, q, _ = np.matmul(self._matrix, [u.magnitude, v.magnitude, 1.0])
                    return p*u.units, q*v.units

            else:
                if len(u)!=len(v):
                    raise ValueError('u and v must be the same length')
                uv = np.ones((3,len(v)))
                if self._units is not None:
                    uv[0,:] = u.to(self._units).magnitude
                    uv[1,:] = v.to(self._units).magnitude
                    pq = np.einsum('ij, jk -> ik', self._matrix, uv)*self._units
                else:
                    uv[0,:] = u.magnitude
                    uv[1,:] = v.magnitude
                    pq = np.einsum('ij, jk -> ik', self._matrix, uv)*u.units
                return pq[0,:], pq[1,:]

        elif isinstance(u,(list,tuple)) and isinstance(v,(list,tuple)):

            if len(u)!=len(v):
                raise ValueError('u and v must be the same length')
            for _u,_v in zip(u,v):
                if not isinstance(_u,pint.Quantity):
                    raise TypeError("u and v must be a sequence container of pint.Quantity objects")
                if not isinstance(_v,pint.Quantity):
                    raise TypeError("u and v must be a sequence container of pint.Quantity objects")

            uv = np.ones((3,len(v)))*u[0].units
            uv[0,:] = Q_.from_list(u)
            uv[1,:] = Q_.from_list(v)
            pq = np.einsum('ij, jk -> ik', self._matrix, uv)
            return pq[0,:], pq[1,:]

        else:
            raise TypeError("u and v must be a pint.Quantity object or a sequence container of pint.Quantity objects")


    @property
    def matrix(self):
        """Get the transformation matrix"""
        if self._matrix is None:
            self.build_matrix()
        return self._matrix

    def build_matrix(self):
        """Rebuild the transformation matrix starting with an identity matrix"""
        self._matrix = np.identity(3)
        for op in self._operations:
            self._matrix = np.matmul(self._matrix, op.matrix)

    def skewX(self, angle: pint.Quantity):
        """Add a X-axis skew transformation"""
        self._operations.insert(0,SkewX(angle))
        return self

    def skewY(self, angle: pint.Quantity):
        """Add a Y-axis skew transformation"""
        self._operations.insert(0,SkewY(angle))
        return self

    def rotate(self, angle: pint.Quantity, x: pint.Quantity=None, y: pint.Quantity=None):
        """Add a rotation transformation"""
        self._operations.insert(0,Rotate(angle, x=x, y=y))
        if x is not None and y is not None:
            if self._units is not None:
                if not x.check(self._units) or not y.check(self._units):
                    raise ValueError("x and y must have the same units as those already in the transform object")
            else:
                self._units = x.units
        return self

    def translate(self, tx: pint.Quantity, ty: pint.Quantity):
        """Add a translation transformation"""
        self._operations.insert(0,Translate(tx, ty))
        if tx is not None and ty is not None:
            if self._units is not None:
                if not tx.check(self._units) or not ty.check(self._units):
                    raise ValueError("x and y must have the same units as those already in the transform object")
            else:
                self._units = tx.units
        return self

    def scale(self, sx: float, sy: float):
        """Add a scale transformation"""
        self._operations.insert(0,Scale(sx,sy))
        return self

    def shear(self, sx: float, sy: float):
        """Add a shear transformation"""
        self._operations.insert(0,Shear(sx,sy))
        return self

    def reflect(self):
        """Add a reflection (about both axes) transformation"""
        self._operations.insert(0,Reflect())
        return self

    def reflectX(self):
        """Add an X-axis reflection transformation"""
        self._operations.insert(0,ReflectX())
        return self

    def reflectY(self):
        """Add a Y-axis reflection transformation"""
        self._operations.insert(0,ReflectY())
        return self

    def sixmatrix(self, a: float, b: float, c: float, d: float, e: float, f: float):
        """Add an arbitrary transformation matrix"""
        self._operations.insert(0,SixMatrix(a, b, c, d, e, f))
        return self


class SkewX:
    """X-axis skew transformation"""
    def __init__(self, angle: pint.Quantity):
        if not isinstance(angle,pint.Quantity):
            raise TypeError("skew angles must be pint.Quantities")
        if not angle.check("[angle]"):
            raise TypeError("skew angles must be pint.Quantities that are angular units")
        self._angle = angle

    def __str__(self):
        return 'skewX({})'.format(self._angle)

    @property
    def matrix(self):
        return np.array([[1.0, math.tan(self._angle.to(ureg.radians)), 0.0], [0, 1.0, 0.0], [0, 0, 1]])


class SkewY:
    """Y-axis skew transformation"""
    def __init__(self, angle: pint.Quantity):
        if not isinstance(angle,pint.Quantity):
            raise TypeError("skew angles must be pint.Quantities")
        if not angle.check("[angle]"):
            raise TypeError("skew angles must be pint.Quantities that are angular units")
        self._angle = angle

    def __str__(self):
        return 'skewY({})'.format(self._angle.to(ureg.degree))

    @property
    def matrix(self):
        return np.array([[1.0, 0.0, 0.0], [math.tan(self._angle.to(ureg.radians)), 1.0, 0.0], [0, 0, 1]])


class Translate:
    """Translation transformation"""
    def __init__(self, x: pint.Quantity, y: pint.Quantity):
        if not isinstance(x,pint.Quantity) or not isinstance(y,pint.Quantity):
            raise TypeError("translation must be pint.Quantities")
        if not (x.check("[length]") or x.check("[pixel]") or x.check("[device]")):
            raise TypeError("translation must be pint.Quantities that are length, pixel or device units")
        if not (x.units==y.units):
            raise ValueError("x and y must have the same units")
        self._x = x
        self._y = y

    def __str__(self):
        return 'translate({} {})'.format(_tostr(self._x), _tostr(self._y))

    @property
    def matrix(self):
        return np.array([[1.0, 0, self._x.magnitude], [0, 1.0, self._y.magnitude], [0, 0, 1]])


class Scale:
    """Scale transformation"""
    def __init__(self, sx: float, sy: float):
        self._sx = sx
        self._sy = sy

    def __str__(self):
        return 'scale({} {})'.format(self._sx, self._sy)

    @property
    def matrix(self):
        return np.array([[self._sx, 0, 0], [0, self._sy, 0], [0, 0, 1]])


class Rotate:
    """Rotation transformation"""
    def __init__(self, angle: pint.Quantity, x: pint.Quantity=None, y: pint.Quantity=None):
        if (x is not None) != (y is not None):
             raise ValueError("Must specify both x and y")
        if x is not None and y is not None:
            if not x.check("[length]") or not x.check("[pixel]") or not x.check("[device]"):
                raise TypeError("origin must be pint.Quantities that are length, pixel or device units")
            if not isinstance(x,pint.Quantity) or not isinstance(y,pint.Quantity):
                raise TypeError("origin must be pint.Quantities")
            if not isinstance(x,pint.Quantity) or not isinstance(y,pint.Quantity):
                raise TypeError("origin must be pint.Quantities")
            if not (x.units==y.units):
                raise ValueError("x and y must have the same units")
        if not isinstance(angle,pint.Quantity):
            raise TypeError("angle must be pint.Quantity")
        if not angle.check("[angle]"):
            raise ValueError("angle must be a pint.Quantity with an angular unit")

        self._x = x
        self._y = y
        self._angle = angle

    def __str__(self):
        if self._x is None or self._y is None:
            return 'rotate({})'.format(self._angle.to(ureg.degree))
        else:
            return 'rotate({} {} {})'.format(self._angle.to(ureg.degree), _tostr(self._x), _tostr(self._y))

    @property
    def matrix(self):
        if self._x is not None:
            return np.array([[math.cos(self._angle.to(ureg.rad).magnitude), -math.sin(self._angle.to(ureg.rad).magnitude), 0],
                            [math.sin(self._angle.to(ureg.rad).magnitude), math.cos(self._angle.to(ureg.rad).magnitude), 0],
                            [self._x.magnitude, self._y.magnitude, 1]])
        else:
            return np.array([[math.cos(self._angle.to(ureg.rad).magnitude), -math.sin(self._angle.to(ureg.rad).magnitude), 0],
                            [math.sin(self._angle.to(ureg.rad).magnitude), math.cos(self._angle.to(ureg.rad).magnitude), 0],
                            [0.0, 0.0, 1.0]])

class Shear:
    """Shear transformation"""
    def __init__(self, sx: float, sy: float):
        self._sx = sx
        self._sy = sy

    def __str__(self):
        m = self.matrix
        return 'matrix({} {} {} {} {} {})'.format(
                    m[0,0], m[1,0], m[2,0],
                    m[0,1], m[1,1], m[2,1],
                    m[0,2], m[1,2], m[2,2])

    @property
    def matrix(self):
        return np.array([[1.0, self._sx, 0], [self._sy, 1.0, 0], [0, 0, 1]])


class Reflect(Scale):
    """Reflection transformation about all axes"""
    def __init__(self):
        super(Reflect,self).__init__(-1.0,-1.0)


class ReflectX(Scale):
    """Reflection transformation about X axis"""
    def __init__(self):
        super(ReflectX,self).__init__(-1.0,1.0)


class ReflectY(Scale):
    """Reflection transformation about Y axis"""
    def __init__(self):
        super(ReflectY,self).__init__(1.0,-1.0)


class SixMatrix:
    """Specify matrix transformation from six parameters"""
    def __init__(self, a: float, b: float, c: float, d: float, e: float, f: float):
        self._matrix = np.array([[a, c, e], [b, d, f], [0, 0, 1]])

    def __str__(self):
        return 'matrix({} {} {} {} {} {})'.format(
                    self._matrix[0,0], self._matrix[1,0], self._matrix[2,0],
                    self._matrix[0,1], self._matrix[1,1], self._matrix[2,1],
                    self._matrix[0,2], self._matrix[1,2], self._matrix[2,2])

    @property
    def matrix(self):
        return self._matrix


class GdalTransform(SixMatrix):
    """Specify matrix transformation from GDAL geom parameters"""
    def __init__(self, geom: Union[List,Tuple,np.ndarray]):
        super(GdalTransform, self).__init__(geom[1], geom[4], geom[2], geom[5], geom[0], geom[3])


def identity():
    """Return an empty affine transformation with an identity matrix"""
    return Affine()
