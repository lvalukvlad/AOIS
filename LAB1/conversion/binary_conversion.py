def int_to_bin(n, bits):
    if n == 0:
        return '0' * bits
    res = []
    num = abs(n)
    for i in range(bits):
        res.append('1' if num & (1 << (bits - 1 - i)) else '0')
    return ''.join(res)

def bin_to_int(b):
    return sum((1 << (len(b) - 1 - i)) for i, bit in enumerate(b) if bit == '1')