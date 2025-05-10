import unittest
from logic.binary_converter import BinaryConverter

class TestBinaryConverter(unittest.TestCase):
    def test_convert_to_binary(self):
        self.assertEqual(BinaryConverter.convert_to_binary(5, 4), [0, 1, 0, 1])
        self.assertEqual(BinaryConverter.convert_to_binary(0, 3), [0, 0, 0])
        self.assertEqual(BinaryConverter.convert_to_binary(7, 3), [1, 1, 1])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            BinaryConverter.convert_to_binary(-1, 2)
        with self.assertRaises(ValueError):
            BinaryConverter.convert_to_binary(8, 3)

if __name__ == '__main__':
    unittest.main()