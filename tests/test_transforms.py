import unittest
import schediazo.transforms

class TestAffine(unittest.TestCase):

	def test_translate_rotate(self):
		aff_translate = schediazo.transforms.identity().translate(1.0,0.0)
		aff_rotate = schediazo.transforms.identity().rotate(90.0)
		x, y = aff_translate(0.0,0.0)
		x, y = aff_rotate(x, y)
		self.assertAlmostEqual(x, 0.0)
		self.assertAlmostEqual(y, 1.0)
	
		aff = schediazo.transforms.identity().translate(1.0,0.0).rotate(90.0)
		print(aff)
		x, y = aff(0.0,0.0)
		self.assertAlmostEqual(x, 0.0)
		self.assertAlmostEqual(y, 1.0)
	

	def test(self):
		aff = schediazo.transforms.identity().translate(-104000, -800500).scale(1/1000, 1/1000)
		xp = [100000, 104000, 105000, 104100]		# m
		yp = [800800, 800900, 800000, 800100]		# m
		up, vp = aff(xp, yp)
		self.assertAlmostEqual(up[0], (100000-104000)/1000)
		self.assertAlmostEqual(up[1], (104000-104000)/1000)
		self.assertAlmostEqual(up[2], (105000-104000)/1000)
		self.assertAlmostEqual(up[3], (104100-104000)/1000)
		self.assertAlmostEqual(vp[0], (800800-800500)/1000)
		self.assertAlmostEqual(vp[1], (800900-800500)/1000)
		self.assertAlmostEqual(vp[2], (800000-800500)/1000)
		self.assertAlmostEqual(vp[3], (800100-800500)/1000)

	def test_six(self):
		# Based on https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform
		aff = schediazo.transforms.identity().sixmatrix(3, 1, -1, 3, 30, 40)

		# (10, 10) -> (50,80)
		p, q = aff(10, 10)
		self.assertAlmostEqual(p, 50)
		self.assertAlmostEqual(q, 80)

		# (40, 10) -> (140,110)
		p, q = aff(40, 10)
		self.assertAlmostEqual(p, 140)
		self.assertAlmostEqual(q, 110)

		# (10, 30) -> (30,140)
		p, q = aff(10, 30)
		self.assertAlmostEqual(p, 30)
		self.assertAlmostEqual(q, 140)

		# (40, 30) -> (120,170)
		p, q = aff(40, 30)
		self.assertAlmostEqual(p, 120)
		self.assertAlmostEqual(q, 170)



if __name__ == '__main__':
	unittest.main()
