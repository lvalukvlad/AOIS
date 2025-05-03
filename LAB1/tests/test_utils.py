import unittest
import io
import sys
from unittest.mock import patch
from utils import get_integer_input, get_float_input, print_number_info


class TestUtils(unittest.TestCase):
    @patch('builtins.input', return_value='5')
    def test_get_integer_input_valid(self, mock_input):
        self.assertEqual(get_integer_input(""), 5)

    @patch('builtins.input', side_effect=['abc', '5'])
    def test_get_integer_input_invalid_then_valid(self, mock_input):
        self.assertEqual(get_integer_input(""), 5)

    @patch('builtins.input', return_value='3.14')
    def test_get_float_input_valid(self, mock_input):
        self.assertEqual(get_float_input(""), 3.14)

    def test_print_number_info(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_number_info(5, 8)
        sys.stdout = sys.__stdout__
        self.assertIn("Прямой код: [0 0000101]", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()