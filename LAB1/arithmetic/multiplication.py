def multiply_direct(a, b, bits=8):
    try:
        def is_special_zero(x):
            if isinstance(x, str):
                return x.strip() in ['-0', 'special_neg_zero']
            return False

        a_is_zero = is_special_zero(a) or a == 0
        b_is_zero = is_special_zero(b) or b == 0

        if a_is_zero or b_is_zero:
            a_neg = is_special_zero(a) or (isinstance(a, int) and a == 0 and str(a).startswith('-'))
            b_neg = is_special_zero(b) or (isinstance(b, int) and b == 0 and str(b).startswith('-'))
            sign = '1' if (a_neg ^ b_neg) else '0'

            decimal_result = "-0" if sign == '1' else "0"
            return f"[{sign} {'0' * (bits - 1)}]", decimal_result

        a_num = int(a) if isinstance(a, str) and a not in ['-0', 'special_neg_zero'] else a
        b_num = int(b) if isinstance(b, str) and b not in ['-0', 'special_neg_zero'] else b

        sign = '1' if (a_num < 0) ^ (b_num < 0) else '0'
        abs_a = abs(a_num)
        abs_b = abs(b_num)

        max_val = 2 ** (bits - 1) - 1
        if abs_a > max_val or abs_b > max_val:
            raise ValueError("Число вне допустимого диапазона")

        result = abs_a * abs_b
        if result > max_val:
            raise OverflowError("Переполнение результата")

        binary = bin(result)[2:].zfill(bits - 1)
        numerical_result = -result if sign == '1' else result

        return f"[{sign} {binary}]", numerical_result

    except Exception as e:
        return f"Ошибка: {str(e)}", None