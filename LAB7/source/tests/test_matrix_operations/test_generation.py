import unittest
from unittest.mock import patch, call
from source.matrix_operations.generation import create_binary_grid, display_grid

class TestMatrixGeneration(unittest.TestCase):
    @patch('random.getrandbits')
    def test_matrix_creation(self, mock_randbits):
        mock_randbits.side_effect = [i % 2 for i in range(16*16)]

        matrix = create_binary_grid()

        self.assertEqual(len(matrix), 16)
        self.assertTrue(all(len(row) == 16 for row in matrix))

        expected_value = 0
        for row in matrix:
            for cell in row:
                self.assertEqual(cell, expected_value % 2)
                expected_value += 1

        self.assertEqual(mock_randbits.call_count, 16*16)

    @patch('builtins.print')
    def test_display(self, mock_print):
        test_matrix = [[0, 1], [1, 0]]

        display_grid(test_matrix, bits_per_row=2)

        expected_calls = [
            call(" 0: 0 1"),
            call(" 1: 1 0")
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)