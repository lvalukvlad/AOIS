import unittest
from logic.sdnf_processing.dnf_calculation import DNFCalculationMinimizer


class TestDNFCaclulation(unittest.TestCase):
    def test_minimization(self):
        minimizer = DNFCalculationMinimizer("(!a & b) | (a & !b) | (a & b)")
        result = minimizer.minimize()

        self.assertTrue(
            result == "(a) | (b)" or result == "(b) | (a)",
            f"Unexpected result: {result}"
        )


if __name__ == '__main__':
    unittest.main()