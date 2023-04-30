"""Transformation classes and functions
"""
from typing import List, Tuple, Union
import math
import numpy as np



class Affine:
    """Affine (scaling/translation) transforms from (u,v) to (p,q)"""
    def __init__(self):
        self._matrix = None
        self._operations = []

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

    def __call__(self, u: Union[float,List,np.ndarray,Tuple], v: Union[float,List,np.ndarray,Tuple]):
        return self.transform(u, v)

    def transform(self, u: Union[float,List,np.ndarray,Tuple], v: Union[float,List,np.ndarray,Tuple]):
        """Transform some points given by u and v coordinates"""
        if self._matrix is None:
            self.build_matrix()

        if isinstance(u,(list,np.ndarray,tuple)) and isinstance(v,(list,np.ndarray,tuple)):
            if len(u)==len(v):
                uv = np.ones((3,len(v)))
                uv[0,:] = u
                uv[1,:] = v
            else:
                raise ValueError('u and v must be the same length')
            pq = np.einsum('ij, jk -> ik', self._matrix, uv)

            return pq[0,:], pq[1,:]
        else:
            p, q, _ = np.matmul(self._matrix, [u, v, 1.0])
        return p, q

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

    def skewX(self, angle: float):
        """Add a X-axis skew transformation"""
        self._operations.insert(0,SkewX(angle))
        return self

    def skewY(self, angle: float):
        """Add a Y-axis skew transformation"""
        self._operations.insert(0,SkewY(angle))
        return self

    def rotate(self, angle: float, x: float=None, y: float=None):
        """Add a rotation transformation"""
        self._operations.insert(0,Rotate(angle, x=x, y=y))
        return self

    def translate(self, tx: float, ty: float):
        """Add a translation transformation"""
        self._operations.insert(0,Translate(tx, ty))
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
    def __init__(self, angle: float):
        self._angle = angle

    def __str__(self):
        return 'skewX({})'.format(self._angle)

    @property
    def matrix(self):
        return np.array([[1.0, math.tan(math.radians(self._angle)), 0.0], [0, 1.0, 0.0], [0, 0, 1]])


class SkewY:
    """Y-axis skew transformation"""
    def __init__(self, angle: float):
        self._angle = angle

    def __str__(self):
        return 'skewY({})'.format(self._angle)

    @property
    def matrix(self):
        return np.array([[1.0, 0.0, 0.0], [math.tan(math.radians(self._angle)), 1.0, 0.0], [0, 0, 1]])


class Translate:
    """Translation transformation"""
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __str__(self):
        return 'translate({} {})'.format(self._x, self._y)

    @property
    def matrix(self):
        return np.array([[1.0, 0, self._x], [0, 1.0, self._y], [0, 0, 1]])


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
    def __init__(self, angle: float, x: float=None, y: float=None):
        if (x is not None) != (y is not None):
             raise ValueError

        self._x = x
        self._y = y
        self._angle = angle

    def __str__(self):
        if self._x is None or self._y is None:
            return 'rotate({})'.format(self._angle)
        else:
            return 'rotate({} {} {})'.format(self._angle, self._x, self._y)

    @property
    def matrix(self):
        return np.array([[math.cos(math.radians(self._angle)), -math.sin(math.radians(self._angle)), 0],
                        [math.sin(math.radians(self._angle)), math.cos(math.radians(self._angle)), 0],
                        [0, 0, 1]])


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
