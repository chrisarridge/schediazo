"""Unit conversions from various dimensions"""

# class UnitConversion:
# 	def __init__(self, m):
# 		self._scale = m*72/25.4e-3

# 	def __mul__(self, v):
# 		return v*self._scale

# 	def __rmul__(self, v):
# 		return v*self._scale

# """Default conversions that people will probably want to use most often"""
# mm = UnitConversion(1e-3)
# inch = UnitConversion(25.4e-3)
# cm = UnitConversion(1e-2)
# m = UnitConversion(1.0)


from pint import UnitRegistry
ureg = UnitRegistry(filename=None)

# Prefixes.
ureg.define("micro- = 1e-6  = µ- = μ- = u-")
ureg.define("milli- = 1e-3  = m-")
ureg.define("centi- = 1e-2  = c-")
ureg.define("deci- =  1e-1  = d-")
ureg.define("deca- =  1e+1  = da- = deka-")
ureg.define("hecto- = 1e2   = h-")
ureg.define("kilo- =  1e3   = k-")

# Basic lengths.
ureg.define("meter = [length] = m = metre")
ureg.define("pixel = [length] = px = pix")

# Imperial lengths.
ureg.define("inch = 25.4 * mm = in")
ureg.define("foot = 12 * inch = ft")

# Publishing/drawing lengths.
ureg.define("point = (1.0/72.0)*inch = pt")
ureg.define("pica = (1.0/6.0)*inch = pc")

Q_ = ureg.Quantity

cm = ureg.cm
mm = ureg.mm
m = ureg.m
inch = ureg.inch
pt = ureg.pt
pc = ureg.pc
