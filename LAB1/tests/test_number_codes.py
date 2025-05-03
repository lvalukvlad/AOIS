import unittest
from conversion.number_codes import direct_code, reverse_code, complement_code


class TestNumberCodes(unittest.TestCase):
    # Тесты для прямого кода (direct code)
    def test_direct_code_positive(self):
        self.assertEqual(direct_code(5, 8), '00000101')

    def test_direct_code_negative(self):
        self.assertEqual(direct_code(-5, 8), '10000101')

    def test_direct_zero(self):
        self.assertEqual(direct_code(0, 8), '00000000')

    def test_direct_negative_zero(self):
        self.assertEqual(direct_code(0, 8, True), '10000000')

    def test_direct_max_positive(self):
        self.assertEqual(direct_code(127, 8), '01111111')

    def test_direct_min_negative(self):
        self.assertEqual(direct_code(-127, 8), '11111111')

    def test_direct_code_invalid_bits(self):
        with self.assertRaises(ValueError):
            direct_code(128, 8)  # Слишком большое число для 8 бит

    # Тесты для обратного кода (reverse code)
    def test_reverse_code_positive(self):
        self.assertEqual(reverse_code(5, 8), '00000101')

    def test_reverse_code_negative(self):
        self.assertEqual(reverse_code(-5, 8), '11111010')

    def test_reverse_zero(self):
        self.assertEqual(reverse_code(0, 8), '00000000')

    def test_reverse_negative_zero(self):
        self.assertEqual(reverse_code(0, 8, True), '11111111')

    def test_reverse_max_positive(self):
        self.assertEqual(reverse_code(127, 8), '01111111')

    def test_reverse_min_negative(self):
        self.assertEqual(reverse_code(-127, 8), '10000000')

    # Тесты для дополнительного кода (two's complement)
    def test_complement_code_positive(self):
        self.assertEqual(complement_code(5, 8), '00000101')

    def test_complement_code_negative(self):
        self.assertEqual(complement_code(-5, 8), '11111011')

    def test_complement_zero(self):
        self.assertEqual(complement_code(0, 8), '00000000')

    def test_complement_negative_zero(self):
        self.assertEqual(complement_code(0, 8, True), '00000000')  # В доп. коде нет -0

    def test_complement_min_value(self):
        self.assertEqual(complement_code(-128, 8), '10000000')  # Крайний случай для 8 бит

    def test_complement_max_value(self):
        self.assertEqual(complement_code(127, 8), '01111111')

    def test_complement_overflow(self):
        with self.assertRaises(ValueError):
            complement_code(128, 8)  # Слишком большое число для 8 бит

    def test_complement_underflow(self):
        with self.assertRaises(ValueError):
            complement_code(-129, 8)  # Слишком маленькое число для 8 бит


if __name__ == '__main__':
    unittest.main()