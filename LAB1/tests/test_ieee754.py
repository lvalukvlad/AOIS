import unittest
from conversion.ieee754 import float_to_ieee754, ieee754_to_float


class TestIEEE754(unittest.TestCase):
    def test_float_conversion_positive(self):
        num = 3.14
        ieee = float_to_ieee754(num)
        converted = ieee754_to_float(ieee)
        self.assertAlmostEqual(converted, num, places=6)

    def test_float_conversion_negative(self):
        num = -123.456
        ieee = float_to_ieee754(num)
        converted = ieee754_to_float(ieee)
        self.assertAlmostEqual(converted, num, places=4)

    def test_float_conversion_zero(self):
        ieee = float_to_ieee754(0.0)
        self.assertEqual(ieee, '0' * 32)


if __name__ == '__main__':
    unittest.main()