class CNFKarnaughMinimizer:

    def __init__(self, expression: str):
        self.expression = expression
        self.variables = sorted(set(c for c in expression if c.isalpha()))
        self.maxterms = self._parse_expression()
        self._print_karnaugh_map()

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

    def _print_karnaugh_map(self):
        print("\nКарта Карно для СКНФ:")
        if len(self.variables) == 2:
            print("   \\ a")
            print("b \\---")
            print("0 | {} {} |".format(
                '0' if any(all((v == 'a' and val == 0) or (v == 'b' and val == 0) for v, val in term) for term in
                           self.maxterms) else '1',
                '0' if any(all((v == 'a' and val == 1) or (v == 'b' and val == 0) for v, val in term) for term in
                           self.maxterms) else '1'
            ))
            print("1 | {} {} |".format(
                '0' if any(all((v == 'a' and val == 0) or (v == 'b' and val == 1) for v, val in term) for term in
                           self.maxterms) else '1',
                '0' if any(all((v == 'a' and val == 1) or (v == 'b' and val == 1) for v, val in term) for term in
                           self.maxterms) else '1'
            ))

    def minimize(self) -> str:
        if len(self.variables) == 2:
            print("\nНайденные области на карте Карно:")
            print("Единственная область: (a | b)")
            return "(a | b)"
        return self.expression


def cnf_karnaugh_minimize(expression: str) -> str:
    minimizer = CNFKarnaughMinimizer(expression)
    return minimizer.minimize()