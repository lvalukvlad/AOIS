from itertools import product, combinations
from collections import defaultdict


class CNFCalculationMinimizer:

    def __init__(self, expression: str):
        self.expression = expression
        self.variables = sorted(set(c for c in expression if c.isalpha()))
        self.maxterms = self._get_maxterms()
        self.prime_implicants = set()
        self._print_initial_sknf()

    def _get_maxterms(self) -> list:
        clauses = self.expression.split('&')
        maxterms = []

        for clause in clauses:
            clause = clause.strip('() ')
            literals = clause.split('|')
            term = []
            for lit in literals:
                lit = lit.strip()
                if lit.startswith('!'):
                    term.append((lit[1:], 1))
                else:
                    term.append((lit, 0))
            maxterms.append(term)
        return maxterms

    def _print_initial_sknf(self):
        print("\nИсходная СКНФ:")
        print(self.expression)
        print("\nЭтапы склеивания:")

    def _try_merge(self, term1, term2):
        diff = [(var, val1, val2) for (var, val1), (v, val2) in zip(term1, term2)
                if val1 != val2 and var == v]
        if len(diff) == 1:
            var, _, _ = diff[0]
            merged = [(v, val) for (v, val) in term1 if v != var]
            merged += [(var, '-')]
            merged.sort()
            return merged
        return None

    def minimize(self) -> str:
        current_terms = self.maxterms.copy()
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
            if val == 0:
                parts.append(var)
            elif val == 1:
                parts.append(f"!{var}")
        return " | ".join(parts)

    def _get_result(self) -> str:
        print("\nПростые импликанты:")
        result_terms = []
        for term in self.prime_implicants:
            term_str = self._term_to_str(term)
            print(term_str)
            result_terms.append(f"({term_str})")

        return " & ".join(result_terms)


def cnf_calc_minimize(expression: str) -> str:
    minimizer = CNFCalculationMinimizer(expression)
    return minimizer.minimize()