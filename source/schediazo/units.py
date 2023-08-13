"""Unit conversions from various dimensions"""
from typing import Union, List

import numpy as np
import pint

ureg = pint.UnitRegistry(filename=None)


# Prefixes.
ureg.define("micro- = 1e-6  = µ- = μ- = u-")
ureg.define("milli- = 1e-3  = m-")
ureg.define("centi- = 1e-2  = c-")
ureg.define("deci- =  1e-1  = d-")
ureg.define("deca- =  1e+1  = da- = deka-")
ureg.define("hecto- = 1e2   = h-")
ureg.define("kilo- =  1e3   = k-")

# Basic lengths.
ureg.define("px = [pixel]")
ureg.define("meter = [length] = m = metre")
ureg.define("percent = [percentage] = %")
ureg.define("device = [device]")

# Imperial lengths.
ureg.define("inch = 25.4 * mm = in")
ureg.define("foot = 12 * inch = ft")

# Publishing/drawing lengths.
ureg.define("point = (1.0/72.0)*inch = pt")
ureg.define("pica = (1.0/6.0)*inch = pc")

# Angles.
ureg.define("pi     = 3.1415926535897932384626433832795028841971693993751 = π  # pi")
ureg.define("radian = [] = rad")
ureg.define("degree = π / 180 * radian = deg = arcdeg = arcdegree = angular_degree")

Q_ = ureg.Quantity

cm = ureg.cm
mm = ureg.mm
inch = ureg.inch
pt = ureg.pt
pc = ureg.pc
rad = ureg.rad
deg = ureg.deg
px = ureg.px
percent = ureg.percent


def _tostr(q: pint.Quantity) -> str:
    """Convert a length-type or % quantity to a string suitable for SVG.

    Parameters
    ----------
    q : pint.Quantity
        Quantity that should have dimensions of [length], [pixel] or be a percentage.

    Returns
    -------
    str
        Formatted string.

    Raises
    ------
    ValueError
        If the quantity doesn't have the right units/dimensions, e.g., a time.
    """
    if q.check("[length]"):
        return ("{:f~P}".format(q)).replace(" ","")
    if q.check("[pixel]"):
        return ("{:f~P}".format(q)).replace(" ","")
    elif q.check(ureg.percent):
        return ("{:f~P}".format(q)).replace(" ","")
    else:
        raise ValueError("Cannot convert these units <{}> to a string for SVG".format(q.units))


def _scale(v: pint.Quantity, device_per_length: pint.Quantity, device_per_pixel: pint.Quantity) -> pint.Quantity:
    """Scale a quantity into device coordinates.

    Parameters
    ----------
    v : pint.Quantity
        Quantity to scale.
    device_per_length : pint.Quantity
        Scaling for physical lengths into device coordinates.
    device_per_pixel : pint.Quantity
        Scaling for pixels into device coordinates.

    Returns
    -------
    pint.Quantity
        Value in device coordinates.

    Raises
    ------
    ValueError
        If the units cannot be scaled.
    """
    
    if v.check("[length]"):
        return (v*device_per_length).to(ureg.device)
    elif v.check("[pixel]"):
        return (v*device_per_pixel).to(ureg.device)
    else:
        raise ValueError

