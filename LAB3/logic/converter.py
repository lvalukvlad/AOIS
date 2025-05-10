def convert_binary_string_to_number(binary_string: str) -> int:
    if not all(char in '01' for char in binary_string):
        raise ValueError("Строка должна содержать только 0 и 1")

    result = 0
    length = len(binary_string)

    for position, bit in enumerate(binary_string):
        exponent = length - position - 1
        result += int(bit) * (1 << exponent)

    return result


def test_conversion():
    test_cases = {
        '0': 0,
        '1': 1,
        '10': 2,
        '101': 5,
        '1111': 15,
        '10000': 16
    }

    for binary, expected in test_cases.items():
        assert convert_binary_string_to_number(binary) == expected, \
            f"Ошибка для {binary}: ожидалось {expected}"

    print("Все тесты пройдены успешно!")


if __name__ == '__main__':
    test_conversion()