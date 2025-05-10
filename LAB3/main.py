import sys
from pathlib import Path

project_root = str(Path(__file__).parent.resolve())
sys.path.insert(0, project_root)

from logic.karnaugh_map import build_truth_table
from logic.converter import convert_binary_string_to_number
from logic.expression_parser import ExpressionParser
from logic.scnf_processing.cnf_calculation import cnf_calc_minimize
from logic.sdnf_processing.dnf_calculation import dnf_calc_minimize
from logic.sdnf_processing.dnf_calc_table import dnf_table_minimize
from logic.scnf_processing.cnf_calc_table import cnf_table_minimize
from logic.scnf_processing.cnf_karnaugh import cnf_karnaugh_minimize
from logic.sdnf_processing.dnf_karnaugh import dnf_karnaugh_minimize

def display_results(variables, rpn, table_data):
    decimal_form = convert_binary_string_to_number(table_data['index_form'])

    print("\nРезультаты анализа логической функции:")
    print(f"Используемые переменные: {', '.join(sorted(set(variables)))}")
    print(f"Обратная польская запись: {' '.join(rpn)}")
    print(f"\nИндексная форма: {table_data['index_form']} (десятичное: {decimal_form})")
    print(f"Числовая форма СДНФ: {table_data['dnf_numeric']}")
    print(f"Числовая форма СКНФ: {table_data['cnf_numeric']}")
    print(f"\nСДНФ: {table_data['dnf_expression']}")
    print(f"СКНФ: {table_data['cnf_expression']}")


def display_minimization_results(dnf_calc, cnf_calc, dnf_table, cnf_table, dnf_karnaugh, cnf_karnaugh):
    print("\nРезультаты минимизации:")
    print(f"1. СДНФ (расчетный метод): {dnf_calc}")
    print(f"2. СКНФ (расчетный метод): {cnf_calc}")
    print(f"3. СДНФ (расчетно-табличный): {dnf_table}")
    print(f"4. СКНФ (расчетно-табличный): {cnf_table}")
    print(f"5. СДНФ (Карно): {dnf_karnaugh}")
    print(f"6. СКНФ (Карно): {cnf_karnaugh}")


def get_valid_expression():
    while True:
        try:
            user_expr = input("\nВведите логическое выражение (или 'q' для выхода): ").strip()

            if user_expr.lower() == 'q':
                print("Выход из программы...")
                exit()

            if not user_expr:
                raise ValueError("Выражение не может быть пустым")

            variables, rpn = ExpressionParser.parse_expression(user_expr)

            if not variables:
                raise ValueError("В выражении должны быть переменные (a, b, c, d, e)")

            return user_expr

        except Exception as e:
            print(f"\nОшибка: {str(e)}")
            print("Пожалуйста, введите выражение снова.")
            print("Примеры допустимых выражений:")
            print("a & (b | !c)")
            print("(a | b) & (!a | c)")
            print("a -> b")
            print("a ~ b")


def main():
    print("Программа для минимизации логических выражений")
    print("Доступные переменные: a, b, c, d, e")
    print("Поддерживаемые операторы: !, &, |, ->, ~")
    print("Для выхода введите 'q'")

    while True:
        try:
            user_expr = get_valid_expression()

            variables, rpn_notation = ExpressionParser.parse_expression(user_expr)

            truth_table = build_truth_table(user_expr, rpn_notation, variables)

            display_results(variables, rpn_notation, truth_table)

            dnf_calc_result = dnf_calc_minimize(truth_table['dnf_expression'])
            cnf_calc_result = cnf_calc_minimize(truth_table['cnf_expression'])
            dnf_table_result = dnf_table_minimize(truth_table['dnf_expression'])
            cnf_table_result = cnf_table_minimize(truth_table['cnf_expression'])
            dnf_karnaugh_result = dnf_karnaugh_minimize(truth_table['dnf_expression'])
            cnf_karnaugh_result = cnf_karnaugh_minimize(truth_table['cnf_expression'])

            display_minimization_results(
                dnf_calc_result, cnf_calc_result,
                dnf_table_result, cnf_table_result,
                dnf_karnaugh_result, cnf_karnaugh_result
            )

            choice = input("\nХотите ввести другое выражение? (y/n): ").strip().lower()
            if choice != 'y':
                print("Выход из программы...")
                break

        except Exception as e:
            print(f"\nНеожиданная ошибка: {str(e)}")
            print("Попробуйте ввести выражение снова.")


if __name__ == '__main__':
    main()