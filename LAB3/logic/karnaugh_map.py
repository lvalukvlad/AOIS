import sys
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from logic.binary_converter import convert_to_binary
from logic.expression_parser import ExpressionParser
from logic.logic_operations import LogicOperations

class TruthTableBuilder:

    def __init__(self, expression: str, rpn: list, variables: list):
        self.expression = expression
        self.rpn = rpn
        self.variables = variables
        self.num_vars = len(variables)
        self.rows = 2 ** self.num_vars

    def build_truth_table(self) -> dict:
        index_form = []
        dnf_terms = []
        cnf_terms = []
        dnf_numeric = []
        cnf_numeric = []

        print(f"\nТаблица истинности для выражения: {self.expression}")
        print(" ".join(self.variables) + " | Result")
        print("-" * (len(self.variables) * 2 + 5))

        for row in range(self.rows):
            binary_values = convert_to_binary(row, self.num_vars)
            values = {var: val for var, val in zip(self.variables, binary_values)}
            result = LogicOperations.evaluate_rpn(self.rpn, values)
            index_form.append(str(result))

            row_str = " ".join(map(str, binary_values)) + f" | {result}"
            print(row_str)

            if result == 1:
                dnf_terms.append(self._build_dnf_term(binary_values))
                dnf_numeric.append(str(row))
            else:
                cnf_terms.append(self._build_cnf_term(binary_values))
                cnf_numeric.append(str(row))

        return {
            'index_form': "".join(index_form),
            'dnf_numeric': f"({' ,'.join(dnf_numeric)})",
            'cnf_numeric': f"({' ,'.join(cnf_numeric)})",
            'dnf_expression': " | ".join(f"({term})" for term in dnf_terms),
            'cnf_expression': " & ".join(f"({term})" for term in cnf_terms)
        }

    def _build_dnf_term(self, values: list) -> str:
        terms = []
        for i, val in enumerate(values):
            terms.append(self.variables[i] if val == 1 else f"!{self.variables[i]}")
        return " & ".join(terms)

    def _build_cnf_term(self, values: list) -> str:
        terms = []
        for i, val in enumerate(values):
            terms.append(f"!{self.variables[i]}" if val == 1 else self.variables[i])
        return " | ".join(terms)


def build_truth_table(expression: str, rpn: list, variables: list) -> dict:
    builder = TruthTableBuilder(expression, rpn, variables)
    return builder.build_truth_table()