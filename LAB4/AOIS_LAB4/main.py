from minimized_pdnf_by_calculation_method import minimize_sdnf_by_calculation_method

def bcd_to_bcd_plus_5(a, b, c, d):
    decimal_input = (a << 3) | (b << 2) | (c << 1) | d
    decimal_output = decimal_input + 5
    a_out = (decimal_output >> 3) & 1
    b_out = (decimal_output >> 2) & 1
    c_out = (decimal_output >> 1) & 1
    d_out = decimal_output & 1
    return a_out, b_out, c_out, d_out

def generate_bcd_conversion_table():
    table = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    decimal_input = (a << 3) | (b << 2) | (c << 1) | d
                    if decimal_input > 4:
                        continue
                    a_out, b_out, c_out, d_out = bcd_to_bcd_plus_5(a, b, c, d)
                    table.append([a, b, c, d, a_out, b_out, c_out, d_out])
    return table

def print_main_bcd_table(table):
    print(f"{'Вход (Д8421)':<15}{'Выход (Д8421+5)':<15}")
    print("-" * 30)
    for row in table:
        input_bits = ''.join(str(bit) for bit in row[:4])
        output_bits = ''.join(str(bit) for bit in row[4:])
        print(f"{input_bits:<15}{output_bits:<15}")

def print_truth_table_for_bit(table, bit_index):
    print(f"\nТаблица истинности для выхода {['a','b','c','d'][bit_index]}:")
    print("a b c d | {0}".format(['a','b','c','d'][bit_index]))
    print("-" * 20)
    for row in table:
        inputs = ' '.join(str(bit) for bit in row[:4])
        output_bit = row[4 + bit_index]
        print(f"{inputs} | {output_bit}")

def build_sdnf_for_bit(table, bit_index):
    terms = []
    var_names = ['a', 'b', 'c', 'd']
    for row in table:
        inputs = row[:4]
        output_bit = row[4 + bit_index]
        if output_bit == 1:
            term = []
            for i, val in enumerate(inputs):
                term.append(f"{var_names[i]}" if val else f"!{var_names[i]}")
            terms.append(f"({'&'.join(term)})")
    return '|'.join(terms)

if __name__ == '__main__':
    bcd_table = generate_bcd_conversion_table()
    print_main_bcd_table(bcd_table)

    for i in range(4):
        print_truth_table_for_bit(bcd_table, i)
        sdnf = build_sdnf_for_bit(bcd_table, i)
        print(f"\nСДНФ для выхода {['a','b','c','d'][i]}:")
        print(sdnf)
        minimized = minimize_sdnf_by_calculation_method(sdnf)
        print(f"Минимизированное выражение для {['a','b','c','d'][i]}:")
        print(minimized)
