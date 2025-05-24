from hash_table import HashTable
from utils import load_data_from_file, save_data_to_file


def main():
    ht = HashTable()
    students_data = load_data_from_file('app/data/students.txt')
    for surname, name in students_data:
        try:
            ht.insert(surname, name)
        except Exception as e:
            print(f"Ошибка: {e}")

    while True:
        print("\nМеню:")
        print("1. Показать хеш-таблицу")
        print("2. Найти студента")
        print("3. Добавить студента")
        print("4. Удалить студента")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            ht.display()

        elif choice == '2':
            key = input("Введите фамилию для поиска: ")
            result = ht.search(key)
            if result:
                print(f"Найден: {result['ID']} - {result['Pi']}")
            else:
                print("Студент не найден")

        elif choice == '3':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            try:
                ht.insert(surname, name)
                print("Студент добавлен")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '4':
            key = input("Введите фамилию для удаления: ")
            if ht.delete(key):
                print("Студент удален")
            else:
                print("Студент не найден")

        elif choice == '5':
            print("Выход из программы")
            break

        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()