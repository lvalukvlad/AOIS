def get_integer_input(prompt, bits=8):
    while True:
        value = input(prompt).strip()
        if value.lower() == 'q':
            return None
        if value == '-0':
            return 'special_neg_zero'
        try:
            num = int(value)
            min_val = -2**(bits-1)
            max_val = 2**(bits-1) - 1
            if min_val <= num <= max_val:
                return num
            print(f"Ошибка: число должно быть от {min_val} до {max_val}!")
        except ValueError:
            print("Ошибка: введите целое число!")

def get_float_input(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'q':
                return None
            return float(value)
        except ValueError:
            print("Ошибка: введите число!")


def print_number_info(n, bits, is_float=False):
    try:
        from conversion.number_codes import direct_code, reverse_code, complement_code
        from conversion.ieee754 import float_to_ieee754
        if isinstance(n, str) and n == 'special_neg_zero':
            print("\nЧисло: -0")
            print(f"Прямой код: [1 {'0' * (bits - 1)}]")
            print(f"Обратный код: [1 {'1' * (bits - 1)}]")
            print(f"Дополнительный код: [0 {'0' * (bits - 1)}]")
            return

        if not is_float:
            num = 0 if isinstance(n, str) and n == '-0' else n
            print(f"\nЧисло: {num}")

            try:
                print(f"Прямой код: [{direct_code(num, bits)[0]} {direct_code(num, bits)[1:]}]")
                print(f"Обратный код: [{reverse_code(num, bits)[0]} {reverse_code(num, bits)[1:]}]")
                print(f"Дополнительный код: [{complement_code(num, bits)[0]} {complement_code(num, bits)[1:]}]")
            except ValueError as e:
                print(f"Ошибка преобразования: {e}")
    except Exception as e:
        print(f"Ошибка при выводе информации: {e}")