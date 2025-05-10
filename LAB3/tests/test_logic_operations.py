import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from logic.logic_operations import LogicOperations, perform_operation


class TestLogicOperations(unittest.TestCase):
    def test_all_operations(self):
        # Тестируем все комбинации операций
        self.assertEqual(LogicOperations.perform_and(1, 1), 1)
        self.assertEqual(LogicOperations.perform_and(1, 0), 0)

        self.assertEqual(LogicOperations.perform_or(0, 0), 0)
        self.assertEqual(LogicOperations.perform_or(0, 1), 1)

        self.assertEqual(LogicOperations.perform_not(1), 0)
        self.assertEqual(LogicOperations.perform_not(0), 1)

        self.assertEqual(LogicOperations.perform_implication(0, 0), 1)
        self.assertEqual(LogicOperations.perform_implication(1, 0), 0)

        self.assertEqual(LogicOperations.perform_equivalence(1, 1), 1)
        self.assertEqual(LogicOperations.perform_equivalence(1, 0), 0)

    def test_evaluate_rpn(self):
        rpn = ['a', 'b', '&', 'c', '|']
        values = {'a': 1, 'b': 0, 'c': 1}
        self.assertEqual(LogicOperations.evaluate_rpn(rpn, values), 1)

    def test_perform_operation_wrapper(self):
        self.assertEqual(perform_operation(1, 0, '&'), 0)
        self.assertEqual(perform_operation(1, None, '!'), 0)


if __name__ == '__main__':
    unittest.main()