from arithmetic.addition import add_complement
from arithmetic.subtraction import subtract_complement
from arithmetic.multiplication import multiply_direct
from arithmetic.division import divide_direct
from arithmetic.float_operations import add_float
from conversion.number_codes import direct_code
from utils import get_integer_input, get_float_input, print_number_info


def print_menu():
    print("\nВыберите операцию:")
    print("1. Перевод числа в прямой, обратный и дополнительный коды")
    print("2. Сложение двух чисел в дополнительном коде")
    print("3. Вычитание двух чисел через дополнительный код")
    print("4. Умножение двух чисел в прямом коде")
    print("5. Деление двух чисел в прямом коде")
    print("6. Сложение двух чисел с плавающей точкой (IEEE-754)")
    print("0. Выход")


def main():
    bits = 8

    while True:
        print_menu()
        choice = input("Ваш выбор (0-6 или 'q' для выхода): ")

        if choice == '0' or choice.lower() == 'q':
            break

        elif choice == '1':
            print("\n[Перевод числа в коды]")
            while True:
                user_input = input("Введите целое число: ").strip()
                if user_input == '-0':
                    print("Результат для -0:")
                    print_number_info('special_neg_zero', bits)
                    break
                else:
                    try:
                        num = int(user_input)
                        max_num = 2 ** (bits - 1) - 1
                        min_num = -2 ** (bits - 1)
                        if num > max_num or num < min_num:
                            print(f"Ошибка: число должно быть от {min_num} до {max_num}!")
                            continue
                        print(f"Результат для числа {num}:")
                        print_number_info(num, bits)
                        break
                    except ValueError:
                        print("Ошибка: введите целое число!")


        elif choice == '2':
            print("\n[Сложение чисел]")
            a = get_integer_input("Введите первое число (или 'q' для отмены): ", bits)
            if a is None:
                continue
            print_number_info(a, bits)
            b = get_integer_input("Введите второе число (или 'q' для отмены): ", bits)
            if b is None:
                continue
            print_number_info(b, bits)
            try:
                res_bin, res_dec = add_complement(a, b, bits)
                print("\nРезультат сложения:")
                print(f"Десятичный: {res_dec}")
                print(f"Дополнительный код результата: {res_bin}")
                if a != 'special_neg_zero' and b != 'special_neg_zero':
                    print_number_info(res_dec, bits)
            except OverflowError:
                print("Ошибка: произошло арифметическое переполнение!")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception:
                print("Произошла непредвиденная ошибка при сложении")

        elif choice == '3':
            print("\n[Вычитание чисел]")
            a = get_integer_input("Введите уменьшаемое (или 'q' для отмены): ", bits)
            if a is None: continue
            print_number_info(a, bits)
            b = get_integer_input("Введите вычитаемое (или 'q' для отмены): ", bits)
            if b is None: continue
            print_number_info(b, bits)
            try:
                res_bin, res_dec = subtract_complement(a, b, bits)
                print("\nРезультат вычитания:")
                print(f"Десятичный: {res_dec}")
                print(f"Дополнительный код результата: {res_bin}")
                if not (a == -128 and (b == 0 or b == 'special_neg_zero')):
                    print_number_info(res_dec, bits)
            except OverflowError:
                print("Ошибка: произошло арифметическое переполнение!")
            except Exception as e:
                print(f"Ошибка при вычитании: {str(e)}")

        elif choice == '4':
            print("\n[Умножение чисел]")
            a = get_integer_input("Введите первый множитель: ")
            if a is None: continue
            print_number_info(a, bits)
            b = get_integer_input("Введите второй множитель: ")
            if b is None: continue
            print_number_info(b, bits)
            res_bin, res_dec = multiply_direct(a, b, bits)
            print("\nРезультат умножения:")
            if res_dec is not None:
                print(f"Десятичный: {res_dec}")
                print(f"Двоичный (прямой код): {res_bin}")
            else:
                print(res_bin)

        elif choice == '5':
            print("\n[Деление чисел]")
            a = get_integer_input("Введите делимое: ")
            if a is None: continue
            print_number_info(a, bits)

            b = get_integer_input("Введите делитель: ")
            if b is None: continue
            print_number_info(b, bits)
            try:
                res_bin, res_dec = divide_direct(a, b, bits)
                print("\nРезультат деления:")
                print(f"Десятичный: {res_dec:.5f}")
                print(f"Двоичный: {res_bin}")
            except ZeroDivisionError:
                print("Ошибка: деление на ноль!")
            except Exception as e:
                print(f"Ошибка при делении: {e}")

        elif choice == '6':
            print("\n[Сложение чисел с плавающей точкой]")
            a = get_float_input("Введите первое число: ")
            if a is None: continue
            print_number_info(a, 32, is_float=True)
            b = get_float_input("Введите второе число: ")
            if b is None: continue
            print_number_info(b, 32, is_float=True)
            res_bin, res_dec = add_float(a, b)
            print("\nРезультат сложения:")
            print(f"Десятичный: {res_dec:.6f}")
            print(f"IEEE-754: {res_bin[:1]} {res_bin[1:9]} {res_bin[9:]}")
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()