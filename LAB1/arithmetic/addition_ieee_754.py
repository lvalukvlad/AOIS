import struct

def float_to_ieee_754(value):
    packed = struct.pack('>f', value)
    integer = struct.unpack('>I', packed)[0]
    binary = bin(integer)[2:].zfill(32)
    return binary

def ieee_754_to_float(binary):
    integer = int(binary, 2)
    packed = struct.pack('>I', integer)
    value = struct.unpack('>f', packed)[0]
    return value

def add_float(a, b):
    bin_a = float_to_ieee_754(a)
    bin_b = float_to_ieee_754(b)

    float_a = ieee_754_to_float(bin_a)
    float_b = ieee_754_to_float(bin_b)

    result = float_a + float_b
    result_bin = float_to_ieee_754(result)
    return result_bin, result
