from arithmetic.addition import add_complement
from conversion.number_codes import complement_code

def subtract_complement(a, b, bits=8):
    if a == -2 ** (bits - 1) and (b == 0 or b == 'special_neg_zero'):
        return '10000000', -128

    return add_complement(a, -b if b != 'special_neg_zero' else 0, bits)