import unittest
from conversion.binary_conversion import int_to_bin, bin_to_int


class TestBinaryConversion(unittest.TestCase):
    def test_int_to_bin_positive(self):
        self.assertEqual(int_to_bin(5, 8), '00000101')

    def test_int_to_bin_zero(self):
        self.assertEqual(int_to_bin(0, 8), '00000000')

    def test_int_to_bin_negative(self):
        self.assertEqual(int_to_bin(-5, 8), '00000101')

    def test_bin_to_int_positive(self):
        self.assertEqual(bin_to_int('00000101'), 5)

    def test_bin_to_int_negative(self):
        self.assertEqual(bin_to_int('10000101'), 133)  # 128 + 4 + 1 = 133

    def test_int_to_bin_edge_cases(self):
        self.assertEqual(int_to_bin(255, 8), '11111111')
        self.assertEqual(int_to_bin(0, 8), '00000000')
        self.assertEqual(int_to_bin(128, 8), '10000000')

if __name__ == '__main__':
    unittest.main()