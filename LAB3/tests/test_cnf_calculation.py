import unittest
from logic.scnf_processing.cnf_calculation import CNFCalculationMinimizer

class TestCNFCalculation(unittest.TestCase):
    def test_minimization(self):
        minimizer = CNFCalculationMinimizer("(a | b)")
        result = minimizer.minimize()
        self.assertEqual(result, "(a | b)")

if __name__ == '__main__':
    unittest.main()