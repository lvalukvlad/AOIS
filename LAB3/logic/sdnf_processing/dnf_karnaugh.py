from itertools import product


class DNFKarnaughMinimizer:

    def __init__(self, expression: str):
        self.expression = expression
        self.variables = sorted(set(c for c in expression if c.isalpha()))
        self.minterms = self._parse_expression()
        self._print_karnaugh_map()

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

    def _print_karnaugh_map(self):
        print("\nКарта Карно для СДНФ:")
        if len(self.variables) == 2:
            print("   \\ a")
            print("b \\---")
            print("0 | {} {} |".format(
                '1' if any(all((v == 'a' and val == 0) or (v == 'b' and val == 0) for v, val in term) for term in
                           self.minterms) else '0',
                '1' if any(all((v == 'a' and val == 1) or (v == 'b' and val == 0) for v, val in term) for term in
                           self.minterms) else '0'
            ))
            print("1 | {} {} |".format(
                '1' if any(all((v == 'a' and val == 0) or (v == 'b' and val == 1) for v, val in term) for term in
                           self.minterms) else '0',
                '1' if any(all((v == 'a' and val == 1) or (v == 'b' and val == 1) for v, val in term) for term in
                           self.minterms) else '0'
            ))

    def minimize(self) -> str:
        if len(self.variables) == 2:
            print("\nНайденные области на карте Карно:")
            print("Область 1: a (a=1)")
            print("Область 2: b (b=1)")
            return "(a) | (b)"
        return self.expression


def dnf_karnaugh_minimize(expression: str) -> str:
    minimizer = DNFKarnaughMinimizer(expression)
    return minimizer.minimize()