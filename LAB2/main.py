def generate_combinations(variables):
    n = len(variables)
    for i in range(2**n):
        yield tuple((i >> (n - 1 - j)) & 1 for j in range(n))

def int_to_bin(num, length):
    return ''.join(str((num >> i) & 1) for i in range(length-1, -1, -1))

OPERATORS = {'!': 3, '&': 2, '|': 1, '~': 0.5, '->': 0}
BINARY_OPERATORS = {'&', '|', '~', '->'}

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        if expression[i] in '()abcde':
            tokens.append(expression[i])
            i += 1
        elif expression[i] == '-' and i + 1 < len(expression) and expression[i + 1] == '>':
            tokens.append('->')
            i += 2
        elif expression[i] in OPERATORS:
            tokens.append(expression[i])
            i += 1
        else:
            raise ValueError(f"Недопустимый символ: {expression[i]}")
    return tokens

def to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token in 'abcde':
            output.append(token)
        elif token == '!':
            stack.append(token)
        elif token in BINARY_OPERATORS:
            while stack and stack[-1] != '(' and OPERATORS.get(stack[-1], 0) >= OPERATORS[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несбалансированные скобки")
            stack.pop()  # убираем '('
    while stack:
        if stack[-1] == '(':
            raise ValueError("Несбалансированные скобки")
        output.append(stack.pop())
    return output

def eval_postfix(postfix, values):
    stack = []
    steps = {}
    step_count = 1

    for token in postfix:
        if token in 'abcde':
            stack.append((token, values[token]))
        elif token == '!':
            a_name, a_val = stack.pop()
            res = int(not a_val)
            step_name = f"¬{a_name}"
            steps[step_name] = res
            stack.append((step_name, res))
        elif token in BINARY_OPERATORS:
            b_name, b_val = stack.pop()
            a_name, a_val = stack.pop()

            if token == '&':
                res = a_val & b_val
                step_name = f"({a_name}∧{b_name})"
            elif token == '|':
                res = a_val | b_val
                step_name = f"({a_name}∨{b_name})"
            elif token == '~':
                res = int(a_val == b_val)
                step_name = f"({a_name}≡{b_name})"
            elif token == '->':
                res = int((not a_val) | b_val)
                step_name = f"({a_name}→{b_name})"

            steps[step_name] = res
            stack.append((step_name, res))

    if len(stack) != 1:
        raise ValueError("Ошибка вычисления")

    return {**values, **steps, 'result': stack[0][1]}


def parse_expression(expression):
    return sorted(set([c for c in expression if c in 'abcde']))


def prettify_expression(expression):
    return expression.replace('!', '¬').replace('&', '∧').replace('|', '∨').replace('~', '≡').replace('->', '→')


def generate_truth_table(expression):
    variables = parse_expression(expression)
    tokens = tokenize(expression)
    postfix = to_postfix(tokens)

    test_values = {var: 0 for var in variables}
    test_result = eval_postfix(postfix, test_values)
    step_headers = [key for key in test_result.keys() if key not in variables and key != 'result']

    table = []
    for row in generate_combinations(variables):
        values = dict(zip(variables, row))
        full_row = eval_postfix(postfix, values)
        table.append(full_row)

    headers = variables + step_headers + ['result']
    return headers, list(reversed(table))


def build_sdnf(variables, table):
    terms = []
    indices = []
    for i, row in enumerate(table):
        if row['result'] == 1:
            indices.append(i)
            parts = []
            for var in variables:
                if var in row:
                    parts.append(var if row[var] else f'¬{var}')
            if parts:
                terms.append(' ∧ '.join(parts))
    return ' ∨ '.join(f'({t})' for t in terms) if terms else None, indices

def build_sknf(variables, table):
    terms = []
    indices = []
    for i, row in enumerate(table):
        if row['result'] == 0:
            indices.append(i)
            parts = []
            for var in variables:
                if var in row:
                    parts.append(f'¬{var}' if row[var] else var)
            if parts:
                terms.append(' ∨ '.join(parts))
    return ' ∧ '.join(f'({t})' for t in terms) if terms else None, indices


def build_index_form(table):
    index = sum(row['result'] << (len(table) - 1 - i) for i, row in enumerate(table))
    return int(''.join(str(row['result']) for row in table), 2)


def print_table(headers, table):
    col_widths = {key: max(len(str(key)), max(len(str(row.get(key, ''))) for row in table)) for key in headers}
    format_row = lambda row: " | ".join(f"{str(row.get(h, '')).rjust(col_widths[h])}" for h in headers)
    header_line = format_row({h: h for h in headers})
    print(header_line)
    print("-" * len(header_line))
    for row in table:
        print(format_row(row))


def main():
    print("Программа для анализа логических выражений")
    print("Допустимые переменные: a, b, c, d, e")
    print("Операторы: ! & | ~ ->")
    print("Введите 'exit' для выхода\n")

    while True:
        expr = input(f"\nВведите логическое выражение: ").strip()
        if expr.lower() == 'exit':
            break

        try:
            pretty = prettify_expression(expr)
            print(f"\nВы ввели выражение:\n\"{pretty}\"\n")

            headers, table = generate_truth_table(expr)
            print("Таблица истинности:")
            print_table(headers, table)

            variables = parse_expression(expr)
            sdnf, sdnf_nums = build_sdnf(variables, table)
            sknf, sknf_nums = build_sknf(variables, table)

            print("\nСДНФ:", sdnf if sdnf else "Не существует (функция всегда ложна)")
            print("СКНФ:", sknf if sknf else "Не существует (функция всегда истинна)")

            print("\nЧисловые формы:")
            print("СДНФ:", " ∨ ".join(map(str, sdnf_nums)) if sdnf_nums else "Не существует")
            print("СКНФ:", " ∧ ".join(map(str, sknf_nums)) if sknf_nums else "Не существует")

            index = build_index_form(table)
            print(f"\nИндексная форма (десятичное): {index}")
            print(f"Индексная форма (двоичное): {bin(index)[2:].zfill(len(table))}")

        except Exception as e:
            print(f"Ошибка: {e}")

    print("Программа завершена.")


if __name__ == "__main__":
    main()