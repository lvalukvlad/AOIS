import unittest
from arithmetic.addition import add_complement
from arithmetic.subtraction import subtract_complement
from arithmetic.multiplication import multiply_direct
from arithmetic.division import divide_direct


class TestArithmetic(unittest.TestCase):
    def test_add_complement_positive(self):
        res, dec = add_complement(5, 3, 8)
        self.assertEqual(dec, 8)

    def test_add_complement_negative(self):
        res, dec = add_complement(-5, -3, 8)
        self.assertEqual(dec, -8)

    def test_subtract_complement(self):
        res, dec = subtract_complement(5, 3, 8)
        self.assertEqual(dec, 2)

    def test_multiply_direct(self):
        res, dec = multiply_direct(5, 3, 8)
        self.assertEqual(dec, 15)

    def test_divide_direct(self):
        res, dec = divide_direct(10, 2, 8)
        self.assertAlmostEqual(dec, 5.0)

    def test_add_complement_overflow(self):
        with self.assertRaises(OverflowError):
            add_complement(127, 1, 8)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_direct(5, 0, 8)

if __name__ == '__main__':
    unittest.main()