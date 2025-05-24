from typing import Any
from source.matrix_operations.generation import create_binary_grid, display_grid
from source.data_access.words import get_diagonal_word
from source.data_access.columns import extract_diagonal_column
from source.matrix_operations.logic import execute_logical_ops
from source.matrix_operations.arithmetic import perform_arithmetic
from source.matrix_operations.sorting import sort_matrix_columns


class MatrixProcessor:
    def __init__(self):
        self.matrix = create_binary_grid()
        self.menu_options = {
            1: self.generate_new_matrix,
            2: self.read_operations,
            3: self.logic_operations,
            4: self.sorting_operation,
            5: self.math_operations,
            0: self.exit_program
        }

    def display_main_menu(self) -> None:
        print("\nМеню процессора матриц:")
        print("1 - Создать новую матрицу")
        print("2 - Операции чтения")
        print("3 - Логические операции")
        print("4 - Сортировка матрицы")
        print("5 - Арифметические операции")
        print("0 - Выход")

    def generate_new_matrix(self) -> None:
        self.matrix = create_binary_grid()
        print("\nНовая матрица создана:")
        display_grid(self.matrix)

    def read_operations(self) -> None:
        print("\nОперации чтения:")
        print("1 - Чтение столбца")
        print("2 - Чтение слова")
        sub_choice = self.get_user_input("Выберите операцию (1-2): ", int, [1, 2])

        if sub_choice == 1:
            self.read_column()
        else:
            self.read_word()

    def read_column(self) -> None:
        col_num = self.get_user_input("Введите номер столбца (0-15): ", int, range(16))
        print(f"\nСтолбец {col_num}:")
        print(extract_diagonal_column(self.matrix, col_num))

    def read_word(self) -> None:
        word_num = self.get_user_input("Введите номер слова (0-15): ", int, range(16))
        print(f"\nСлово {word_num}:")
        print(get_diagonal_word(self.matrix, word_num))

    def logic_operations(self) -> None:
        print("\nЛогические операции:")
        word1 = self.get_user_input("Введите номер первого слова (0-15): ", int, range(16))
        word2 = self.get_user_input("Введите номер второго слова (0-15): ", int, range(16))

        data1 = get_diagonal_word(self.matrix, word1)
        data2 = get_diagonal_word(self.matrix, word2)

        print(f"\nСлово {word1}: {data1}")
        print(f"Слово {word2}: {data2}")
        execute_logical_ops(data1, data2)

    def sorting_operation(self) -> None:
        print("\nСортировка столбцов матрицы...")
        sort_matrix_columns(self.matrix)
        display_grid(self.matrix)

    def math_operations(self) -> None:
        print("\nВведите 3-битный ключ (0 или 1 для каждого бита):")
        key = [
            self.get_user_input(f"Бит {i + 1} (0/1): ", int, [0, 1])
            for i in range(3)
        ]

        perform_arithmetic(self.matrix, key)
        print("\nМатрица после арифметических операций:")
        display_grid(self.matrix)

    def exit_program(self) -> None:
        print("Завершение работы программы...")

    @staticmethod
    def get_user_input(prompt: str, type_func: Any, valid_range: Any) -> Any:
        while True:
            try:
                value = type_func(input(prompt))
                if value in valid_range:
                    return value
                print("Некорректный ввод. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("Некорректный формат ввода. Пожалуйста, попробуйте снова.")

    def run(self) -> None:
        while True:
            self.display_main_menu()
            choice = self.get_user_input("Введите ваш выбор (0-5): ", int, range(6))

            if choice == 0:
                self.menu_options[choice]()
                break

            self.menu_options[choice]()


if __name__ == '__main__':
    processor = MatrixProcessor()
    processor.run()