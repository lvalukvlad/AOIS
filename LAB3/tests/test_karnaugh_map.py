import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

from logic.expression_parser import ExpressionParser
from logic.karnaugh_map import TruthTableBuilder


class TestKarnaughMap(unittest.TestCase):
    def setUp(self):
        self.vars, self.rpn = ExpressionParser.parse_expression("a | b")

    def test_truth_table_builder(self):
        builder = TruthTableBuilder("a | b", self.rpn, self.vars)
        table = builder.build_truth_table()

        self.assertEqual(table['index_form'], "0111")
        self.assertEqual(table['dnf_numeric'], "(1 ,2 ,3)")
        self.assertEqual(table['cnf_numeric'], "(0)")

        # Проверяем построение термов
        self.assertIn("(!a & b)", table['dnf_expression'])
        self.assertIn("(a | b)", table['cnf_expression'])

    def test_build_dnf_term(self):
        builder = TruthTableBuilder("a | b", self.rpn, self.vars)
        term = builder._build_dnf_term([0, 1])
        self.assertEqual(term, "!a & b")

    def test_build_cnf_term(self):
        builder = TruthTableBuilder("a | b", self.rpn, self.vars)
        term = builder._build_cnf_term([0, 1])
        self.assertEqual(term, "a | !b")


if __name__ == '__main__':
    unittest.main()