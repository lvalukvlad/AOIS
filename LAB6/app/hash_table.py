class HashTable:
    def __init__(self, size=20):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function1(self, key):
        russian_alphabet = {
            'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ё': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10,
            'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15, 'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20,
            'Ф': 21, 'Х': 22, 'Ц': 23, 'Ч': 24, 'Ш': 25, 'Щ': 26, 'Ъ': 27, 'Ы': 28, 'Ь': 29, 'Э': 30,
            'Ю': 31, 'Я': 32
        }

        first_char = key[0].upper() if len(key) > 0 else 'А'
        second_char = key[1].upper() if len(key) > 1 else 'А'

        v1 = russian_alphabet.get(first_char, 0)
        v2 = russian_alphabet.get(second_char, 0)

        return v1 * 33 + v2

    def hash_function2(self, key):
        prime = 7
        V = self.hash_function1(key)
        return prime - (V % prime)

    def get_hash(self, key, attempt=0):
        h1 = self.hash_function1(key) % self.size
        h2 = self.hash_function2(key)
        return (h1 + attempt * h2) % self.size

    def insert(self, key, data):
        if self.count >= self.size:
            raise Exception("Хеш-таблица заполнена")

        attempt = 0
        while attempt < self.size:
            index = self.get_hash(key, attempt)

            if self.table[index] is None or self.table[index]['D'] == 1:
                self.table[index] = {
                    'ID': key,
                    'C': 1 if attempt > 0 else 0,
                    'U': 1,
                    'T': 1,
                    'L': 0,
                    'D': 0,
                    'P0': None,
                    'Pi': data
                }
                self.count += 1
                return index

            if self.table[index]['ID'] == key and self.table[index]['D'] == 0:
                raise Exception(f"Ключ '{key}' уже существует")

            attempt += 1

        raise Exception("Не удалось вставить элемент")

    def search(self, key):
        attempt = 0
        while attempt < self.size:
            index = self.get_hash(key, attempt)

            if self.table[index] is None:
                return None

            if self.table[index]['ID'] == key and self.table[index]['D'] == 0:
                return self.table[index]

            attempt += 1

        return None

    def delete(self, key):
        attempt = 0
        while attempt < self.size:
            index = self.get_hash(key, attempt)

            if self.table[index] is None:
                return False

            if self.table[index]['ID'] == key and self.table[index]['D'] == 0:
                self.table[index]['D'] = 1
                self.count -= 1
                return True

            attempt += 1

        return False

    def display(self):
        print(
            f"{'Индекс':<7} | {'ID':<15} | {'C':<2} | {'U':<2} | {'T':<2} | {'L':<2} | {'D':<2} | {'P0':<5} | {'Pi':<20}")
        print("-" * 80)
        for i in range(self.size):
            if self.table[i] is not None and self.table[i]['D'] == 0:
                row = self.table[i]
                print(
                    f"{i:<7} | {row['ID']:<15} | {row['C']:<2} | {row['U']:<2} | {row['T']:<2} | {row['L']:<2} | {row['D']:<2} | {str(row['P0']):<5} | {str(row['Pi']):<20}")
            elif self.table[i] is not None:
                row = self.table[i]
                print(
                    f"{i:<7} | {row['ID']:<15} | {row['C']:<2} | {row['U']:<2} | {row['T']:<2} | {row['L']:<2} | {row['D']:<2} | {str(row['P0']):<5} | {'(удалено)':<20}")
            else:
                print(
                    f"{i:<7} | {'-':<15} | {'-':<2} | {'-':<2} | {'-':<2} | {'-':<2} | {'-':<2} | {'-':<5} | {'-':<20}")

        print(f"\nКоэффициент заполнения: {self.count / self.size:.2f}")