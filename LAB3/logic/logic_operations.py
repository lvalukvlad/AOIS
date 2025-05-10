class LogicOperations:

    @staticmethod
    def perform_and(a: int, b: int) -> int:
        return 1 if a == 1 and b == 1 else 0

    @staticmethod
    def perform_or(a: int, b: int) -> int:
        return 0 if a == 0 and b == 0 else 1

    @staticmethod
    def perform_not(a: int) -> int:
        return 1 - a

    @staticmethod
    def perform_implication(a: int, b: int) -> int:
        return 0 if a == 1 and b == 0 else 1

    @staticmethod
    def perform_equivalence(a: int, b: int) -> int:
        return 1 if a == b else 0

    @classmethod
    def evaluate_rpn(cls, rpn: list, values: dict) -> int:
        stack = []

        for token in rpn:
            if token in values:
                stack.append(values[token])
            elif token.startswith('!'):
                var = token[1]
                stack.append(cls.perform_not(values[var]))
            else:
                if token == '!':
                    a = stack.pop()
                    stack.append(cls.perform_not(a))
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if token == '&':
                        stack.append(cls.perform_and(a, b))
                    elif token == '|':
                        stack.append(cls.perform_or(a, b))
                    elif token == '->':
                        stack.append(cls.perform_implication(a, b))
                    elif token == '~':
                        stack.append(cls.perform_equivalence(a, b))
                    else:
                        raise ValueError(f"Неизвестный оператор: {token}")

        return stack[0]


def perform_operation(left: int, right: int, operator: str) -> int:
    if operator == '!':
        return LogicOperations.perform_not(right)
    return {
        '&': LogicOperations.perform_and,
        '|': LogicOperations.perform_or,
        '->': LogicOperations.perform_implication,
        '~': LogicOperations.perform_equivalence
    }[operator](left, right)


if __name__ == "__main__":
    test_cases = [
        (1, 1, '&', 1),
        (1, 0, '&', 0),
        (1, 0, '|', 1),
        (0, 0, '|', 0),
        (1, 0, '->', 0),
        (0, 1, '->', 1),
        (1, 1, '~', 1),
        (0, 1, '~', 0),
        (0, None, '!', 1),
        (1, None, '!', 0)
    ]

    for a, b, op, expected in test_cases:
        if op == '!':
            result = perform_operation(None, a, op)
        else:
            result = perform_operation(a, b, op)
        assert result == expected, f"Ошибка: {a} {op} {b} = {result}, ожидалось {expected}"

    print("Все тесты пройдены успешно!")