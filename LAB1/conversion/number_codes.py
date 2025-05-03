from conversion.binary_conversion import int_to_bin, bin_to_int

def direct_code(n, bits, is_negative_zero=False):
    if is_negative_zero or (isinstance(n, str) and n == 'special_neg_zero'):
        return '1' + '0' * (bits - 1)
    if n == 0:
        return '0' * bits
    if n > 0:
        return '0' + int_to_bin(n, bits - 1)
    return '1' + int_to_bin(-n, bits - 1)

def reverse_code(n, bits, is_negative_zero=False):
    if is_negative_zero or (isinstance(n, str) and n == 'special_neg_zero'):
        return '1' + '1' * (bits - 1)
    if n == 0:
        return '0' * bits
    if n > 0:
        return direct_code(n, bits)
    direct = direct_code(n, bits)
    return direct[0] + ''.join('1' if b == '0' else '0' for b in direct[1:])


def complement_code(n, bits=8, is_negative_zero=False):
    min_val = -2 ** (bits - 1)
    max_val = 2 ** (bits - 1) - 1

    if is_negative_zero or (isinstance(n, str) and n == 'special_neg_zero'):
        if bits == 8:
            return '10000000'
        raise ValueError("Отрицательный ноль только для 8 бит")

    if n == -2 ** (bits - 1):
        return '1' + '0' * (bits - 1)

    if not isinstance(n, int):
        raise ValueError("Входное значение должно быть целым числом")

    if not (min_val <= n <= max_val):
        raise ValueError(f"Число {n} вне диапазона [{min_val};{max_val}] для {bits} бит")

    if n == 0:
        return '0' * bits
    if n > 0:
        return '0' + int_to_bin(n, bits - 1)

    abs_bin = int_to_bin(-n, bits - 1)
    inverted = ''.join('1' if b == '0' else '0' for b in abs_bin)
    return '1' + bin(int(inverted, 2) + 1)[2:].zfill(bits - 1)