import unittest
from source.data_access.columns import extract_diagonal_column

class TestColumnOperations(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1 if i == j else 0 for j in range(16)]
            for i in range(16)
        ]

    def test_column_extraction(self):
        column = extract_diagonal_column(self.matrix, 0)
        expected = [1] + [0]*15  # [1, 0, 0, ..., 0]
        self.assertEqual(column, expected)

    def test_wrapping(self):
        column = extract_diagonal_column(self.matrix, 15)
        expected = [0]*15 + [1]  # [0, 0, ..., 0, 1]
        self.assertEqual(column, expected)