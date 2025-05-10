from minimized_pdnf_by_calculation_method import minimize_sdnf_by_calculation_method
def int_to_bin_list(n, width):
    return [int(b) for b in format(n, f'0{width}b')]

def bin_list_to_str(bits):
    return ''.join(str(b) for b in bits)

def get_t_inputs(curr_state, next_state):
    return [int(c != n) for c, n in zip(curr_state, next_state)]

def generate_transition_table():
    table = []
    for i in range(8):
        curr = int_to_bin_list(i, 3)
        next_ = int_to_bin_list((i + 1) % 16, 3)
        t_inputs = get_t_inputs(curr, next_)
        table.append((curr, next_, t_inputs))
    return table

def print_transition_table(table):
    print("a b c | T2 T1 T0")
    print("-------------------------")
    for curr, _, t in table:
        print(f"{bin_list_to_str(curr)}   | {bin_list_to_str(t)}")

def build_logic_expressions(table):
    expressions = [[] for _ in range(3)]
    var_names = ['a', 'b', 'c', 'd']

    for row in table:
        curr_state, _, t_inputs = row
        for i in range(3):
            if t_inputs[i] == 1:
                terms = []
                for j, bit in enumerate(curr_state):
                    var = var_names[j]
                    term = var if bit == 1 else f"!{var}"
                    terms.append(term)
                expressions[i].append('&'.join(terms))
    return expressions

def convert_to_nand_or(expr_list):
    final_exprs = []
    for exprs in expr_list:
        if not exprs:
            final_exprs.append("0")
            continue
        or_expr = '|'.join([f"({e})" for e in exprs])
        final_exprs.append(or_expr)
    return final_exprs

def main():
    table = generate_transition_table()
    print("ТАБЛИЦА ПЕРЕХОДОВ:")
    print_transition_table(table)

    logic_exprs = build_logic_expressions(table)
    nand_or_exprs = convert_to_nand_or(logic_exprs)

    print("\nЛОГИЧЕСКИЕ ВЫРАЖЕНИЯ ДЛЯ ВХОДОВ Т-ТРИГГЕРОВ:")
    for i, expr in enumerate(nand_or_exprs[::-1]):
        print(f"T{i} = {expr}")
        min_met = minimize_sdnf_by_calculation_method(expr)
        print(f'Минимизированная версия: {min_met}')

if __name__ == "__main__":
    main()
