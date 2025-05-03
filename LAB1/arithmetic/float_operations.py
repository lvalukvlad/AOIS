from conversion.ieee754 import float_to_ieee754, ieee754_to_float

def add_float(a, b):
    a_ieee = float_to_ieee754(a)
    b_ieee = float_to_ieee754(b)
    result = ieee754_to_float(a_ieee) + ieee754_to_float(b_ieee)
    result_ieee = float_to_ieee754(result)
    return result_ieee, result