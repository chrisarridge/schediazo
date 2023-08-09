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
ureg.define("px = [display_length]")
ureg.define("meter = [length] = m = metre")
ureg.define("percent = [] = %")

# Imperial lengths.
ureg.define("inch = 25.4 * mm = in")
ureg.define("foot = 12 * inch = ft")

# Publishing/drawing lengths.
ureg.define("point = (1.0/72.0)*inch = pt")
ureg.define("pica = (1.0/6.0)*inch = pc")

Q_ = ureg.Quantity

cm = ureg.cm
mm = ureg.mm
inch = ureg.inch
pt = ureg.pt
pc = ureg.pc

def _tostr(q: pint.Quantity) -> str:
    """Convert a length-type or % quantity to a string suitable for SVG.

    Parameters
    ----------
    q : pint.Quantity
        Quantity that should have dimensions of [length], [display_length] or be a percentage.

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
        return ("{:f~P}".format(q.to(ureg.mm))).replace(" ","")
    if q.check("[display_length]"):
        return ("{:f~P}".format(q.to(ureg.px))).replace(" ","")
    elif q.check(ureg.percent):
        return ("{:f~P}".format(q.to(ureg.percent))).replace(" ","")
    else:
        raise ValueError("Cannot convert these units <{}> to a string for SVG".format(q.units))

