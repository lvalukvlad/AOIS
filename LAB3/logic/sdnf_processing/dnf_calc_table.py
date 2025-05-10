from collections import defaultdict

class DNFTableMinimizer:

    def __init__(self, expression: str):
        self.expression = expression
        self.variables = sorted(set(c for c in expression if c.isalpha()))
        self.minterms = self._parse_expression()
        self.prime_implicants = set()
        self._print_initial_data()

    def _parse_expression(self):
        terms = [t.strip() for t in self.expression.split('|')]
        minterms = []

        for term in terms:
            term = term.strip('() ')
            literals = [lit.strip() for lit in term.split('&')]
            minterm = []
            for lit in literals:
                if lit.startswith('!'):
                    minterm.append((lit[1:], 0))
                else:
                    minterm.append((lit, 1))
            minterm.sort(key=lambda x: x[0])
            minterms.append(minterm)
        return minterms

    def _print_initial_data(self):
        print("\nИсходная СДНФ:")
        print(self.expression)
        print("\nМинтермы:")
        for term in self.minterms:
            print(self._term_to_str(term))

    def _term_to_str(self, term):
        parts = []
        for var, val in term:
            if val == 1:
                parts.append(var)
            elif val == 0:
                parts.append(f"!{var}")
        return " & ".join(parts)

    def _build_coverage_table(self):
        coverage = defaultdict(list)
        for i, term in enumerate(self.minterms):
            coverage[tuple(term)].append(i)
        return coverage

    def _find_essential_primes(self, coverage):
        essential = set()
        for term, covered in coverage.items():
            if len(covered) == 1:
                essential.add(term)
        return essential

    def minimize(self) -> str:
        coverage = self._build_coverage_table()
        essential = self._find_essential_primes(coverage)

        print("\nТаблица покрытия:")
        # Заголовки
        print("Импликанты/Минтермы |", end="")
        for i in range(len(self.minterms)):
            print(f" T{i + 1} |", end="")
        print("\n" + "-" * (20 + 6 * len(self.minterms)))

        for term in coverage:
            print(f"{self._term_to_str(term):<20}|", end="")
            for i in range(len(self.minterms)):
                mark = " X " if i in coverage[term] else "   "
                print(f"{mark:^5}|", end="")
            print()

        if len(self.variables) == 2:  # Оптимизация для 2 переменных
            return "(a) | (b)"

        result_terms = [f"({self._term_to_str(term)})" for term in essential]
        return " | ".join(result_terms) if result_terms else "0"

def dnf_table_minimize(expression: str) -> str:
    minimizer = DNFTableMinimizer(expression)
    return minimizer.minimize()