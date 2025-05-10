from itertools import product
def truth_table_pdnf(expression, variables):
    table = []
    # Заменяем операторы для корректной работы eval()
    expression = expression.replace("!", "not ").replace("&", " and ").replace("|", " or ")

    for values in product([0, 1], repeat=len(variables)):
        env = {var: bool(val) for var, val in zip(variables, values)}
        result = eval(expression, {}, env)  # Теперь eval() понимает выражение
        if result:
            table.append(values)
    return table

def to_sdnf(table, variables):
    terms = []
    for row in table:
        term = []
        for var, val in zip(variables, row):
            term.append(f"!{var}" if val == 0 else var)
        terms.append(" & ".join(term))
    return " | ".join(terms)

def minimize_sdnf_by_calculation_method(expression_str):
    variables = sorted(set(filter(str.isalpha, expression_str)))
    table = truth_table_pdnf(expression_str, variables)
    sdnf = to_sdnf(table, variables)

    # Создание списка термов в строковом представлении
    terms = ["".join(str(int(v)) for v in row) for row in table]

    # Минимизация
    prime_implicants = set()
    while terms:
        new_terms = set()
        used = set()
        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                diffs = [idx for idx in range(len(terms[i])) if terms[i][idx] != terms[j][idx]]
                if len(diffs) == 1:
                    index = diffs[0]
                    new_term = terms[i][:index] + "-" + terms[i][index + 1:]
                    new_terms.add(new_term)
                    used.add(terms[i])
                    used.add(terms[j])
        prime_implicants.update(set(terms) - used)
        terms = list(new_terms)

    minimized_terms = []
    for term in prime_implicants:
        minimized_terms.append('(' + ("&".join(
            f"!{var}" if bit == "0" else var for var, bit in zip(variables, term) if bit != "-"
        )) + ')')

    minimized = "|".join(minimized_terms)
    return minimized