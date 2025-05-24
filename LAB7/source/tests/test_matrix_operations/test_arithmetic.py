import unittest
from source.matrix_operations.arithmetic import perform_arithmetic, binary_sum


class TestArithmeticOperations(unittest.TestCase):
    def setUp(self):
        self.base_matrix = [
            [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # V=111 (первые 3 бита)
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]  # V=000
        ]

        self.carry_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # A=15, B=15
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def test_binary_sum_no_carry(self):
        result = binary_sum([0, 1, 0, 1], [1, 0, 1, 0])  # 5 + 10
        self.assertEqual(result, [0, 1, 1, 1, 1])  # 15 (01111)

    def test_binary_sum_with_carry(self):
        result = binary_sum([1, 1, 1, 1], [1, 1, 1, 1])  # 15 + 15
        self.assertEqual(result, [1, 1, 1, 1, 0])  # 30 (11110)

    def test_binary_sum_edge_cases(self):
        self.assertEqual(binary_sum([0] * 4, [0] * 4), [0] * 5)
        self.assertEqual(binary_sum([1] + [0] * 3, [0] * 4), [0, 0, 0, 0, 1])

    def test_key_match_single_column(self):
        test_matrix = [row.copy() for row in self.base_matrix]
        test_matrix[1][0] = 1

        result = perform_arithmetic(test_matrix, [1, 1, 1])
        self.assertEqual(result[0][11:16], [1, 0, 0, 1, 0])
        self.assertEqual(result[1][11:16], [0, 0, 0, 0, 0])

    def test_key_match_multiple_columns(self):
        test_matrix = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        result = perform_arithmetic(test_matrix, [1, 1, 1])
        for col in range(16):
            self.assertEqual(result[0][col], test_matrix[0][col])
            self.assertEqual(result[1][col], test_matrix[1][col])

    def test_carry_handling(self):
        result = perform_arithmetic([row.copy() for row in self.carry_matrix], [1, 1, 1])
        self.assertEqual(result[0][11:16], [1, 1, 1, 1, 0])

    def test_no_match_preserves_matrix(self):
        original = [row.copy() for row in self.base_matrix]
        result = perform_arithmetic(original, [0, 0, 1])
        self.assertEqual(result, original)

    def test_empty_matrix(self):
        self.assertEqual(perform_arithmetic([], [1, 1, 1]), [])

    def test_invalid_key_length(self):
        with self.assertRaises(ValueError):
            perform_arithmetic(self.base_matrix, [1, 1])

    def test_matrix_with_short_columns(self):
        short_matrix = [
            [1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
        with self.assertRaises(ValueError):
            perform_arithmetic(short_matrix, [1, 1, 1])


if __name__ == '__main__':
    unittest.main()