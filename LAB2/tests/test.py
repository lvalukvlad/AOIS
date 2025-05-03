import unittest
from main import (
    tokenize, to_postfix, eval_postfix,
    parse_expression, prettify_expression,
    generate_combinations, int_to_bin,
    build_sdnf, build_sknf, build_index_form,
    generate_truth_table
)

class TestLogicFunctions(unittest.TestCase):

    def test_tokenize(self):
        self.assertEqual(tokenize("a&b"), ['a', '&', 'b'])
        self.assertEqual(tokenize("a -> b"), ['a', '->', 'b'])  # Оператор '->' как единый токен
        self.assertEqual(tokenize("!(a|b)"), ['!', '(', 'a', '|', 'b', ')'])
        self.assertEqual(tokenize("a~b"), ['a', '~', 'b'])
        with self.assertRaises(ValueError):
            tokenize("a$b")

    def test_to_postfix(self):
        self.assertEqual(to_postfix(['a', '&', 'b']), ['a', 'b', '&'])
        self.assertEqual(to_postfix(['a', '->', 'b']), ['a', 'b', '->'])  # '->' как единый оператор
        self.assertEqual(to_postfix(['!', 'a']), ['a', '!'])
        self.assertEqual(to_postfix(['(', 'a', '|', 'b', ')', '&', 'c']),
                         ['a', 'b', '|', 'c', '&'])
        with self.assertRaises(ValueError):
            to_postfix(['a', '&', 'b', ')'])

    def test_eval_postfix(self):
        values = {'a': 1, 'b': 0}
        self.assertEqual(eval_postfix(['a', 'b', '&'], values)['result'], 0)
        self.assertEqual(eval_postfix(['a', 'b', '|'], values)['result'], 1)
        self.assertEqual(eval_postfix(['a', '!'], values)['result'], 0)
        self.assertEqual(eval_postfix(['a', 'b', '->'], values)['result'], 0)
        self.assertEqual(eval_postfix(['a', 'b', '~'], values)['result'], 0)
        self.assertEqual(eval_postfix(['a', 'b', '~', '!'], values)['result'], 1)

    def test_parse_expression(self):
        self.assertEqual(parse_expression("a&b"), ['a', 'b'])
        self.assertEqual(parse_expression("(a|b)&c"), ['a', 'b', 'c'])
        self.assertEqual(parse_expression("!a"), ['a'])
        self.assertEqual(parse_expression(""), [])

    def test_prettify_expression(self):
        self.assertEqual(prettify_expression("a&b"), "a∧b")
        self.assertEqual(prettify_expression("a|b"), "a∨b")
        self.assertEqual(prettify_expression("a->b"), "a→b")
        self.assertEqual(prettify_expression("a~b"), "a≡b")
        self.assertEqual(prettify_expression("!a"), "¬a")

    def test_generate_combinations(self):
        comb = list(generate_combinations(['a', 'b']))
        self.assertEqual(comb, [(0, 0), (0, 1), (1, 0), (1, 1)])
        comb = list(generate_combinations(['a', 'b', 'c']))
        self.assertEqual(comb, [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)])

    def test_int_to_bin(self):
        self.assertEqual(int_to_bin(5, 4), "0101")
        self.assertEqual(int_to_bin(3, 3), "011")

    def test_build_sdnf_sknf(self):
        table = [
            {'a': 0, 'b': 0, 'result': 0},
            {'a': 0, 'b': 1, 'result': 1},
            {'a': 1, 'b': 0, 'result': 1},
            {'a': 1, 'b': 1, 'result': 1}
        ]
        variables = ['a', 'b']

        sdnf, sdnf_nums = build_sdnf(variables, table)
        self.assertTrue("(¬a ∧ b)" in sdnf)
        self.assertTrue("(a ∧ ¬b)" in sdnf)
        self.assertTrue("(a ∧ b)" in sdnf)
        self.assertEqual(set(sdnf_nums), {1, 2, 3})

        sknf, sknf_nums = build_sknf(variables, table)
        self.assertEqual(sknf, "(a ∨ b)")
        self.assertEqual(sknf_nums, [0])

    def test_build_index_form(self):
        table = [
            {'result': 1},
            {'result': 0},
            {'result': 1},
            {'result': 1}
        ]
        self.assertEqual(build_index_form(table), 11)  # 1011 = 11

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            generate_truth_table("")

class TestIntegration(unittest.TestCase):

    def test_full_workflow(self):
        expr = "a&b"
        variables = parse_expression(expr)
        tokens = tokenize(expr)
        postfix = to_postfix(tokens)

        headers, table = generate_truth_table(expr)
        self.assertEqual(len(table), 4)

        sdnf, _ = build_sdnf(variables, table)
        self.assertTrue("(a ∧ b)" in sdnf)

        sknf, _ = build_sknf(variables, table)
        self.assertTrue("(¬a ∨ ¬b)" in sknf or "(¬a ∨ b)" in sknf)

    def test_complex_expression(self):
        expr = "!(a&b)|(c->d)"
        variables = parse_expression(expr)
        tokens = tokenize(expr)
        postfix = to_postfix(tokens)

        headers, table = generate_truth_table(expr)
        self.assertEqual(len(table), 16)

        sdnf, _ = build_sdnf(variables, table)
        sknf, _ = build_sknf(variables, table)

        self.assertIsNotNone(sdnf)
        self.assertIsNotNone(sknf)


class TestAdditionalCases(unittest.TestCase):

    def test_single_variable(self):
        expr = "a"
        headers, table = generate_truth_table(expr)
        self.assertEqual(len(table), 2)
        self.assertEqual(table[0]['a'], 1)
        self.assertEqual(table[1]['a'], 0)

        sdnf, _ = build_sdnf(['a'], table)
        sknf, _ = build_sknf(['a'], table)
        self.assertEqual(sdnf, "a")
        self.assertEqual(sknf, "a")

    def test_nested_negation(self):
        expr = "!!a"
        headers, table = generate_truth_table(expr)
        self.assertEqual(len(table), 2)
        self.assertEqual(table[0]['result'], 1)
        self.assertEqual(table[1]['result'], 0)

    def test_complex_operations(self):
        expr = "(a & b) -> (!c | d)"
        headers, table = generate_truth_table(expr)
        self.assertEqual(len(table), 16)
        self.assertIn('result', table[0])
        self.assertIn('result', table[-1])

    def test_always_true_false(self):
        expr_true = "a | !a"
        expr_false = "a & !a"

        _, table_true = generate_truth_table(expr_true)
        _, table_false = generate_truth_table(expr_false)

        self.assertTrue(all(row['result'] for row in table_true))
        self.assertTrue(not any(row['result'] for row in table_false))

    def test_variable_order(self):
        expr = "c & b & a"
        variables = parse_expression(expr)
        self.assertEqual(variables, ['a', 'b', 'c'])

    def test_empty_sknf_sdnf(self):
        table_all_true = [{'a': 0, 'result': 1}, {'a': 1, 'result': 1}]
        table_all_false = [{'a': 0, 'result': 0}, {'a': 1, 'result': 0}]

        sdnf_all_true, _ = build_sdnf(['a'], table_all_true)
        sknf_all_false, _ = build_sknf(['a'], table_all_false)

        self.assertIsNone(sdnf_all_true)
        self.assertIsNone(sknf_all_false)

    def test_multiple_negations(self):
        expr = "!!!a"
        tokens = tokenize(expr)
        self.assertEqual(tokens, ['!', '!', '!', 'a'])
        postfix = to_postfix(tokens)
        self.assertEqual(postfix, ['a', '!', '!', '!'])
        res0 = eval_postfix(postfix, {'a': 0})['result']
        res1 = eval_postfix(postfix, {'a': 1})['result']
        self.assertEqual(res0, 1)
        self.assertEqual(res1, 0)

if __name__ == "__main__":
    unittest.main()
