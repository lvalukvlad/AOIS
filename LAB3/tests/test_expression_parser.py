import unittest
from logic.expression_parser import ExpressionParser

class TestExpressionParser(unittest.TestCase):
    def test_parse_simple_expression(self):
        vars, rpn = ExpressionParser.parse_expression("a & b")
        self.assertEqual(vars, ['a', 'b'])
        self.assertEqual(rpn, ['a', 'b', '&'])

    def test_parse_complex_expression(self):
        vars, rpn = ExpressionParser.parse_expression("(a | !b) -> c")
        self.assertEqual(vars, ['a', 'b', 'c'])
        self.assertEqual(rpn, ['a', '!b', '|', 'c', '->'])

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.parse_expression("a &")
        with self.assertRaises(ValueError):
            ExpressionParser.parse_expression("a & 1")  # Неверный символ
        with self.assertRaises(ValueError):
            ExpressionParser.parse_expression("")  # Пустая строка

if __name__ == '__main__':
    unittest.main()