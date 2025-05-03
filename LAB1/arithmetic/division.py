from conversion.binary_conversion import int_to_bin

def divide_direct(a, b, bits, precision=5):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")

    sign = '1' if (a < 0) ^ (b < 0) else '0'
    abs_a = abs(a)
    abs_b = abs(b)

    integer_part = abs_a // abs_b
    remainder = abs_a % abs_b

    fractional = 0.0
    for i in range(1, precision + 1):
        remainder *= 2
        bit = remainder // abs_b
        fractional += bit * (2 ** -i)
        remainder %= abs_b

    result = integer_part + fractional
    if sign == '1':
        result = -result

    int_part_bin = int_to_bin(abs(integer_part), bits)
    frac_part_bin = []
    temp = fractional
    for _ in range(precision):
        temp *= 2
        frac_part_bin.append('1' if temp >= 1.0 else '0')
        if temp >= 1.0:
            temp -= 1.0

    binary_rep = sign + int_part_bin + '.' + ''.join(frac_part_bin)
    return binary_rep, result