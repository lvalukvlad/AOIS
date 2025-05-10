from itertools import combinations
from collections import defaultdict


class DNFCalculationMinimizer:

    def __init__(self, expression: str):
        self.expression = expression
        self.variables = sorted(set(c for c in expression if c.isalpha()))
        self.minterms = self._parse_expression()
        self.prime_implicants = set()
        self._print_initial_dnf()

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
            # Сортируем по имени переменной для корректного сравнения
            minterm.sort(key=lambda x: x[0])
            minterms.append(minterm)
        return minterms

    def _print_initial_dnf(self):
        print("\nИсходная СДНФ:")
        print(self.expression)
        print("\nМинтермы:")
        for term in self.minterms:
            print(self._term_to_str(term))
        print("\nЭтапы склеивания:")

    def _try_merge(self, term1, term2):
        if len(term1) != len(term2):
            return None

        diff = []
        for (var1, val1), (var2, val2) in zip(term1, term2):
            if var1 != var2:
                return None
            if val1 != val2:
                diff.append((var1, val1, val2))

        if len(diff) == 1:
            var, _, _ = diff[0]
            merged = [(v, val) for (v, val) in term1 if v != var]
            merged.append((var, '-'))
            merged.sort(key=lambda x: x[0])
            return merged
        return None

    def minimize(self) -> str:
        current_terms = self.minterms.copy()
        iteration = 1

        while True:
            new_terms = []
            used = set()

            for i, j in combinations(range(len(current_terms)), 2):
                merged = self._try_merge(current_terms[i], current_terms[j])
                if merged:
                    print(
                        f"Этап {iteration}: склеиваем {self._term_to_str(current_terms[i])} и {self._term_to_str(current_terms[j])} -> {self._term_to_str(merged)}")
                    new_terms.append(merged)
                    used.add(i)
                    used.add(j)

            for i, term in enumerate(current_terms):
                if i not in used:
                    self.prime_implicants.add(tuple(term))

            if not new_terms:
                break

            current_terms = new_terms
            iteration += 1

        return self._get_result()

    def _term_to_str(self, term) -> str:
        parts = []
        for var, val in term:
            if val == 1:
                parts.append(var)
            elif val == 0:
                parts.append(f"!{var}")
        return " & ".join(parts)

    def _get_result(self) -> str:
        print("\nПростые импликанты:")
        result_terms = []

        sorted_implicants = sorted([list(t) for t in self.prime_implicants], key=lambda x: (len(x), x[0][0]))

        for term in sorted_implicants:
            term_str = self._term_to_str(term)
            print(term_str)
            result_terms.append(f"({term_str})")

        return " | ".join(result_terms) if result_terms else "0"


def dnf_calc_minimize(expression: str) -> str:
    minimizer = DNFCalculationMinimizer(expression)
    return minimizer.minimize()