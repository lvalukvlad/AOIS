import unittest
from unittest.mock import patch
from source.matrix_operations.sorting import (
    extract_circular_word,
    transpose_matrix,
    compare_bit_sequences,
    sort_matrix_columns,
    perform_ordered_selection
)

class TestMatrixSorting(unittest.TestCase):
    def setUp(self):
        self.sample_16x16 = [
            [1 if (i + j) % 16 == 0 else 0 for j in range(16)]
            for i in range(16)
        ]
        self.small_matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]
        self.empty_matrix = []
        self.single_column = [[0], [1], [0]]

    def test_extract_circular_word_full_length(self):
        data = [i % 2 for i in range(16)]
        result = extract_circular_word(data, 0)
        self.assertEqual(result, data)
        start_pos = 5
        expected = data[start_pos:] + data[:start_pos]
        result = extract_circular_word(data, start_pos)
        self.assertEqual(result, expected)

    def test_extract_circular_word_edge_cases(self):
        self.assertEqual(extract_circular_word([], 0), [])
        short_data = [0, 1]
        expected = [0, 1] + [0] * 14
        self.assertEqual(extract_circular_word(short_data, 0), expected)

    def test_transpose_matrix_square(self):
        matrix = [
            [0, 1],
            [1, 0]
        ]
        expected = [
            [0, 1],
            [1, 0]
        ]
        self.assertEqual(transpose_matrix(matrix), expected)

    def test_transpose_matrix_rectangular(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 1]
        ]
        expected = [
            [0, 1],
            [1, 0],
            [0, 1]
        ]
        self.assertEqual(transpose_matrix(matrix), expected)

    def test_transpose_matrix_edge_cases(self):
        self.assertEqual(transpose_matrix([]), [])
        self.assertEqual(transpose_matrix([[1]]), [[1]])

    def test_compare_bit_sequences(self):
        self.assertTrue(compare_bit_sequences([1, 0], [0, 1], 0))
        self.assertFalse(compare_bit_sequences([1, 0], [1, 0], 0))
        self.assertTrue(compare_bit_sequences([0, 1, 0], [0, 0, 1], 1))

    def test_sort_matrix_columns_small(self):
        expected = [
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ]
        result = sort_matrix_columns(self.small_matrix)
        self.assertEqual(result, expected)

    def test_sort_matrix_columns_large(self):
        result = sort_matrix_columns(self.sample_16x16)
        self.assertEqual(len(result), 16)
        self.assertEqual(len(result[0]), 16)

    def test_sort_matrix_columns_edge_cases(self):
        self.assertEqual(sort_matrix_columns(self.empty_matrix), [])
        self.assertEqual(sort_matrix_columns(self.single_column), self.single_column)

    @patch('source.matrix_operations.sorting.display_grid')
    @patch('source.matrix_operations.sorting.sort_matrix_columns')
    def test_perform_ordered_selection(self, mock_sort, mock_display):
        mock_sort.return_value = self.small_matrix
        result = perform_ordered_selection(self.small_matrix)
        mock_sort.assert_called_once()
        self.assertEqual(mock_display.call_count, 2)
        self.assertEqual(result, self.small_matrix)

    def test_error_handling(self):
        bad_matrix = [[0, 1], [1]]
        with self.assertRaises(Exception):
            sort_matrix_columns(bad_matrix)

if __name__ == '__main__':
    unittest.main()