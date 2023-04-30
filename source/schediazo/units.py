"""Unit conversions from various dimensions into points"""

class UnitConversion:
	def __init__(self, m):
		self._scale = m*72/25.4e-3

	def __mul__(self, v):
		return v*self._scale

	def __rmul__(self, v):
		return v*self._scale

"""Default conversions that people will probably want to use most often"""
mm = UnitConversion(1e-3)
inch = UnitConversion(25.4e-3)
cm = UnitConversion(1e-2)
m = UnitConversion(1.0)
