import unittest
import schediazo.transforms
import schediazo as sc
import numpy as np


class TestAffine(unittest.TestCase):

	def test_transform_with_units(self):
		# Translation with the same units.
		aff = schediazo.transforms.identity().translate(1.0*sc.mm,0.0*sc.mm)
		x, y = aff(0.0*sc.mm, 0.0*sc.mm)
		self.assertEqual(x, 1.0*sc.mm)
		self.assertEqual(y, 0.0*sc.mm)

		x, y = aff(np.array([0.0,1.0])*sc.mm, np.array([0.0,1.0])*sc.mm)
		self.assertEqual(x[0], 1.0*sc.mm)
		self.assertEqual(x[1], 2.0*sc.mm)
		self.assertEqual(y[0], 0.0*sc.mm)
		self.assertEqual(y[1], 1.0*sc.mm)

		x, y = aff([0.0*sc.mm,1.0*sc.mm], [0.0*sc.mm,1.0*sc.mm])
		self.assertEqual(x[0], 1.0*sc.mm)
		self.assertEqual(x[1], 2.0*sc.mm)
		self.assertEqual(y[0], 0.0*sc.mm)
		self.assertEqual(y[1], 1.0*sc.mm)


		aff = schediazo.transforms.identity().translate(1.0*sc.cm,1.0*sc.cm)
		x, y = aff(0.0*sc.mm, 0.0*sc.mm)
		self.assertEqual(x, 1.0*sc.cm)
		self.assertEqual(y, 1.0*sc.cm)

		x, y = aff(np.array([0.0,1.0])*sc.mm, np.array([0.0,1.0])*sc.mm)
		self.assertEqual(x[0], 1.0*sc.cm)
		self.assertEqual(x[1], 1.1*sc.cm)
		self.assertEqual(y[0], 1.0*sc.cm)
		self.assertEqual(y[1], 1.1*sc.cm)


	def test_translate_rotate(self):
		aff_translate = schediazo.transforms.identity().translate(1.0*sc.mm,0.0*sc.mm)
		aff_rotate = schediazo.transforms.identity().rotate(90.0*sc.deg)
		x, y = aff_translate(0.0*sc.mm,0.0*sc.mm)
		x, y = aff_rotate(x, y)
		self.assertAlmostEqual(x, 0.0*sc.mm)
		self.assertAlmostEqual(y, 1.0*sc.mm)
	
		aff = schediazo.transforms.identity().translate(1.0*sc.mm,0.0*sc.mm).rotate(90.0*sc.deg)
		print(aff)
		x, y = aff(0.0*sc.mm,0.0*sc.mm)
		self.assertAlmostEqual(x, 0.0*sc.mm)
		self.assertAlmostEqual(y, 1.0*sc.mm)
	

	def test(self):
		aff = schediazo.transforms.identity().translate(-104000*sc.mm, -800500*sc.mm).scale(1/1000, 1/1000)
		self.assertRaises(TypeError, aff, [1,2], [3,4])
		xp = [100000*sc.mm, 104000*sc.mm, 105000*sc.mm, 104100*sc.mm]		# m
		yp = [800800*sc.mm, 800900*sc.mm, 800000*sc.mm, 800100*sc.mm]		# m
		up, vp = aff(xp, yp)
		self.assertAlmostEqual(up[0], (100000-104000)*sc.mm/1000)
		self.assertAlmostEqual(up[1], (104000-104000)*sc.mm/1000)
		self.assertAlmostEqual(up[2], (105000-104000)*sc.mm/1000)
		self.assertAlmostEqual(up[3], (104100-104000)*sc.mm/1000)
		self.assertAlmostEqual(vp[0], (800800-800500)*sc.mm/1000)
		self.assertAlmostEqual(vp[1], (800900-800500)*sc.mm/1000)
		self.assertAlmostEqual(vp[2], (800000-800500)*sc.mm/1000)
		self.assertAlmostEqual(vp[3], (800100-800500)*sc.mm/1000)

	def test_six(self):
		# Based on https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform
		aff = schediazo.transforms.identity().sixmatrix(3, 1, -1, 3, 30, 40)

		# (10, 10) -> (50,80)
		p, q = aff(10*sc.mm, 10*sc.mm)
		self.assertAlmostEqual(p, 50*sc.mm)
		self.assertAlmostEqual(q, 80*sc.mm)

		# (40, 10) -> (140,110)
		p, q = aff(40*sc.mm, 10*sc.mm)
		self.assertAlmostEqual(p, 140*sc.mm)
		self.assertAlmostEqual(q, 110*sc.mm)

		# (10, 30) -> (30,140)
		p, q = aff(10*sc.mm, 30*sc.mm)
		self.assertAlmostEqual(p, 30*sc.mm)
		self.assertAlmostEqual(q, 140*sc.mm)

		# (40, 30) -> (120,170)
		p, q = aff(40*sc.mm, 30*sc.mm)
		self.assertAlmostEqual(p, 120*sc.mm)
		self.assertAlmostEqual(q, 170*sc.mm)



if __name__ == '__main__':
	unittest.main()
