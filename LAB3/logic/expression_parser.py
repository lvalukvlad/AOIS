class ExpressionParser:

    OPERATOR_PRECEDENCE = {
        '!': 4,  # Отрицание (высший приоритет)
        '&': 3,  # Конъюнкция
        '|': 2,  # Дизъюнкция
        '->': 1,  # Импликация
        '~': 1,  # Эквивалентность
        '(': 0   # Скобка (низший приоритет)
    }

    VARIABLES = {'a', 'b', 'c', 'd', 'e'}

    @staticmethod
    def _is_variable(token: str) -> bool:
        if len(token) == 1:
            return token in ExpressionParser.VARIABLES
        elif len(token) == 2 and token[0] == '!':
            return token[1] in ExpressionParser.VARIABLES
        return False

    @staticmethod
    def _get_operator(token: str, index: int, expr: str) -> tuple:
        if token == '-' and index + 1 < len(expr) and expr[index + 1] == '>':
            return '->', index + 1
        return token, index

    @staticmethod
    def _handle_operator(token: str, output: list, operator_stack: list) -> None:
        while (operator_stack and
               operator_stack[-1] != '(' and
               ExpressionParser.OPERATOR_PRECEDENCE[operator_stack[-1]] >=
               ExpressionParser.OPERATOR_PRECEDENCE[token]):
            output.append(operator_stack.pop())
        operator_stack.append(token)

    @staticmethod
    def _handle_closing_parenthesis(output: list, operator_stack: list) -> None:
        while operator_stack and operator_stack[-1] != '(':
            output.append(operator_stack.pop())
        if operator_stack and operator_stack[-1] == '(':
            operator_stack.pop()

    @classmethod
    def parse_expression(cls, expr: str) -> tuple:
        output = []
        operator_stack = []
        i = 0
        variables = set()

        while i < len(expr):
            token = expr[i]

            if token.isspace():
                i += 1
                continue

            if token in cls.VARIABLES:
                output.append(token)
                variables.add(token)
                i += 1
                continue

            if token == '!' and i + 1 < len(expr) and expr[i + 1] in cls.VARIABLES:
                output.append(f"!{expr[i + 1]}")
                variables.add(expr[i + 1])
                i += 2
                continue

            if token == '(':
                operator_stack.append(token)
                i += 1
                continue

            if token == ')':
                cls._handle_closing_parenthesis(output, operator_stack)
                i += 1
                continue

            if token in {'&', '|', '!', '-', '~'}:
                operator, i = cls._get_operator(token, i, expr)
                cls._handle_operator(operator, output, operator_stack)
                i += 1
                continue

            raise ValueError(f"Неизвестный символ: {token}")

        while operator_stack:
            if operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            else:
                operator_stack.pop()

        return sorted(variables), output


if __name__ == '__main__':
    test_expr = "a & (b | !c) -> d"
    variables, rpn = ExpressionParser.parse_expression(test_expr)
    print(f"Выражение: {test_expr}")
    print(f"Переменные: {variables}")
    print(f"ОПЗ: {rpn}")