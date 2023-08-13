import unittest
import schediazo.units

import unittest
import schediazo.transforms

class TestUnits(unittest.TestCase):
    def test_string_conversion(self):
        self.assertEqual(schediazo.units._tostr(10*schediazo.units.px), "10.000000px")
        self.assertEqual(schediazo.units._tostr(10*schediazo.units.percent), "10.000000%")
        self.assertEqual(schediazo.units._tostr(10*schediazo.units.mm), "10.000000mm")
        self.assertEqual(schediazo.units._tostr(1*schediazo.units.cm), "10.000000mm")

if __name__=='__main__':
    unittest.main()
