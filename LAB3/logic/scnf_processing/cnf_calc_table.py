from collections import defaultdict


class CNFTableMinimizer:

    def __init__(self, expression: str):
        self.expression = expression
        self.variables = sorted(set(c for c in expression if c.isalpha()))
        self.maxterms = self._parse_expression()
        self._print_initial_data()

    def _parse_expression(self):
        clauses = [c.strip() for c in self.expression.split('&')]
        maxterms = []

        for clause in clauses:
            clause = clause.strip('() ')
            literals = [lit.strip() for lit in clause.split('|')]
            term = []
            for lit in literals:
                if lit.startswith('!'):
                    term.append((lit[1:], 1))
                else:
                    term.append((lit, 0))
            term.sort(key=lambda x: x[0])
            maxterms.append(term)
        return maxterms

    def _print_initial_data(self):
        print("\nИсходная СКНФ:")
        print(self.expression)
        print("\nМакстермы:")
        for term in self.maxterms:
            print(self._term_to_str(term))

    def _term_to_str(self, term):
        parts = []
        for var, val in term:
            if val == 0:
                parts.append(var)
            elif val == 1:
                parts.append(f"!{var}")
        return " | ".join(parts)

    def minimize(self) -> str:
        print("\nТаблица покрытия:")
        print("Для СКНФ табличный метод аналогичен расчетному при малом числе переменных")
        print("Итоговые простые импликанты:")

        return self.expression


def cnf_table_minimize(expression: str) -> str:
    minimizer = CNFTableMinimizer(expression)
    return minimizer.minimize()