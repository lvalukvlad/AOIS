from conversion.number_codes import complement_code
from conversion.binary_conversion import bin_to_int

def add_binary(a, b, bits):
    result = []
    carry = 0
    for i in range(bits - 1, -1, -1):
        sum_bits = int(a[i]) + int(b[i]) + carry
        result.append(str(sum_bits % 2))
        carry = sum_bits // 2
    return ''.join(reversed(result)), carry


def add_complement(a, b, bits=8):
    a_num = 0 if a == 'special_neg_zero' else a
    b_num = 0 if b == 'special_neg_zero' else b

    min_val = -2 ** (bits - 1)
    max_val = 2 ** (bits - 1) - 1

    if not (min_val <= a_num <= max_val):
        raise ValueError(f"Первое число вне диапазона [{min_val};{max_val}]")
    if not (min_val <= b_num <= max_val):
        raise ValueError(f"Второе число вне диапазона [{min_val};{max_val}]")

    a_comp = complement_code(a_num, bits)
    b_comp = complement_code(b_num, bits)

    result, carry = add_binary(a_comp, b_comp, bits)

    if a_comp[0] == b_comp[0] and result[0] != a_comp[0]:
        raise OverflowError("Арифметическое переполнение")

    if result[0] == '1':
        inverted = ''.join('1' if b == '0' else '0' for b in result[1:])
        dec = -(bin_to_int(inverted) + 1)
    else:
        dec = bin_to_int(result[1:])

    return result, dec