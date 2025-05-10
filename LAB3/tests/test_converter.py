import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from logic.converter import convert_binary_string_to_number


class TestConverter(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(convert_binary_string_to_number(''), 0)
        self.assertEqual(convert_binary_string_to_number('0'), 0)
        self.assertEqual(convert_binary_string_to_number('1'), 1)

    def test_large_numbers(self):
        self.assertEqual(convert_binary_string_to_number('11111111'), 255)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            convert_binary_string_to_number('012')
        with self.assertRaises(ValueError):
            convert_binary_string_to_number('abc')


if __name__ == '__main__':
    unittest.main()