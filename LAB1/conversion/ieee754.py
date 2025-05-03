from conversion.binary_conversion import int_to_bin, bin_to_int

def float_to_ieee754(f):
    if f == 0.0:
        return '0' * 32

    sign = '1' if f < 0 else '0'
    f = abs(f)

    exponent = 0
    if f >= 2.0:
        while f >= 2.0:
            f /= 2.0
            exponent += 1
    elif f < 1.0:
        while f < 1.0:
            f *= 2.0
            exponent -= 1
    exponent += 127
    exp_bin = format(exponent, '08b')
    mantissa = f - 1.0
    mant_bin = []
    for _ in range(23):
        mantissa *= 2
        mant_bin.append('1' if mantissa >= 1.0 else '0')
        if mantissa >= 1.0:
            mantissa -= 1.0

    return sign + exp_bin + ''.join(mant_bin)

def ieee754_to_float(b):
    if b == '0' * 32:
        return 0.0
    sign = -1 if b[0] == '1' else 1
    exponent = int(b[1:9], 2) - 127
    mantissa = 1.0

    for i, bit in enumerate(b[9:32]):
        if bit == '1':
            mantissa += 2 ** -(i + 1)

    return sign * mantissa * (2 ** exponent)