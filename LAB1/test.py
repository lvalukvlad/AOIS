def test_int_to_bin():
    assert int_to_bin(0, 8) == '00000000'
    assert int_to_bin(5, 8) == '00000101'
    assert int_to_bin(-5, 8) == '11111011'
    assert int_to_bin(127, 8) == '01111111'
    assert int_to_bin(-128, 8) == '10000000'
    print("test_int_to_bin passed")

def test_bin_to_int():
    assert bin_to_int('00000000') == 0
    assert bin_to_int('00000101') == 5
    assert bin_to_int('11111011') == 251  # -5 в дополнительном коде
    assert bin_to_int('01111111') == 127
    assert bin_to_int('10000000') == 128  # -128 в дополнительном коде
    print("test_bin_to_int passed")

def test_direct_code():
    assert direct_code(0, 8) == '00000000'
    assert direct_code(5, 8) == '00000101'
    assert direct_code(-5, 8) == '10000101'
    assert direct_code(127, 8) == '01111111'
    assert direct_code(-128, 8) == '11000000'
    print("test_direct_code passed")

def test_reverse_code():
    assert reverse_code(0, 8) == '00000000'
    assert reverse_code(5, 8) == '00000101'
    assert reverse_code(-5, 8) == '11111010'
    assert reverse_code(127, 8) == '01111111'
    assert reverse_code(-128, 8) == '10111111'
    print("test_reverse_code passed")

def test_complement_code():
    assert complement_code(0, 8) == '00000000'
    assert complement_code(5, 8) == '00000101'
    assert complement_code(-5, 8) == '11111011'
    assert complement_code(127, 8) == '01111111'
    assert complement_code(-128, 8) == '10000000'
    print("test_complement_code passed")

def test_add_binary():
    assert add_binary('00000101', '00000011', 8) == ('00001000', 0)
    assert add_binary('11111011', '00000011', 8) == ('00000000', 1)  # -5 + 3 = -2
    assert add_binary('01111111', '00000001', 8) == ('10000000', 0)  # 127 + 1 = -128
    print("test_add_binary passed")

def test_add_complement():
    assert add_complement(5, 3, 8) == ('00001000', 8)
    assert add_complement(-5, 3, 8) == ('00000000', 0)  # -5 + 3 = -2
    assert add_complement(127, 1, 8) == ('10000000', -128)  # 127 + 1 = -128
    print("test_add_complement passed")

def test_subtract_complement():
    assert subtract_complement(5, 3, 8) == ('00000010', 2)
    assert subtract_complement(-5, 3, 8) == ('11111101', -8)  # -5 - 3 = -8
    assert subtract_complement(127, 1, 8) == ('01111110', 126)  # 127 - 1 = 126
    print("test_subtract_complement passed")

def test_multiply_direct():
    assert multiply_direct(5, 3, 8) == ('00001111', 15)
    assert multiply_direct(-5, 3, 8) == ('11110001', -15)
    assert multiply_direct(127, 1, 8) == ('01111111', 127)
    print("test_multiply_direct passed")

def test_divide_direct():
    assert divide_direct(15, 3, 8) == ('00000111.10000', 5.0)
    assert divide_direct(-15, 3, 8) == ('11111000.10000', -5.0)
    assert divide_direct(127, 1, 8) == ('01111111.00000', 127.0)
    print("test_divide_direct passed")

def test_float_to_ieee754():
    assert float_to_ieee754(0.0) == '0' * 32
    assert float_to_ieee754(1.0) == '00111111100000000000000000000000'
    assert float_to_ieee754(-1.0) == '10111111100000000000000000000000'
    assert float_to_ieee754(0.5) == '00111111000000000000000000000000'
    print("test_float_to_ieee754 passed")

def test_ieee754_to_float():
    assert ieee754_to_float('0' * 32) == 0.0
    assert ieee754_to_float('00111111100000000000000000000000') == 1.0
    assert ieee754_to_float('10111111100000000000000000000000') == -1.0
    assert ieee754_to_float('00111111000000000000000000000000') == 0.5
    print("test_ieee754_to_float passed")

def test_add_float():
    assert add_float(1.0, 2.0) == ('01000000000000000000000000000000', 3.0)
    assert add_float(-1.0, 2.0) == ('00111111100000000000000000000000', 1.0)
    assert add_float(0.5, 0.5) == ('00111111100000000000000000000000', 1.0)
    print("test_add_float passed")

def run_tests():
    test_int_to_bin()
    test_bin_to_int()
    test_direct_code()
    test_reverse_code()
    test_complement_code()
    test_add_binary()
    test_add_complement()
    test_subtract_complement()
    test_multiply_direct()
    test_divide_direct()
    test_float_to_ieee754()
    test_ieee754_to_float()
    test_add_float()
    print("All tests passed!")

run_tests()
