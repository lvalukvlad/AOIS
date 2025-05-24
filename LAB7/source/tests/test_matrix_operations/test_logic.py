import unittest
from source.matrix_operations.logic import execute_logical_ops

class TestLogicOperations(unittest.TestCase):
    def test_logic_operations_standard(self):
        a = [0, 0, 1, 1]
        b = [0, 1, 0, 1]

        expected = {
            'XOR': [0, 1, 1, 0],
            'Equivalence': [1, 0, 0, 1],
            'Inhibition': [0, 1, 0, 0],
            'Implication': [1, 1, 0, 1]
        }

        result = execute_logical_ops(a, b)
        self.assertEqual(result, expected)

    def test_logic_operations_edge_cases(self):
        test_cases = [
            ([], [], [], [], [], []),
            ([1], [0], [1], [0], [0], [0]),
            ([1,1], [0,0], [1,1], [0,0], [0,0], [0,0]),
            ([1,0], [1,0], [0,0], [1,1], [0,0], [1,1])
        ]

        for a, b, exp_xor, exp_equiv, exp_inhibit, exp_impl in test_cases:
            with self.subTest(a=a, b=b):
                result = execute_logical_ops(a, b)
                self.assertEqual(result['XOR'], exp_xor)
                self.assertEqual(result['Equivalence'], exp_equiv)
                self.assertEqual(result['Inhibition'], exp_inhibit)
                self.assertEqual(result['Implication'], exp_impl)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            execute_logical_ops([0, 1], [0])