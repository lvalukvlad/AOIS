def load_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) >= 2:
                        key = parts[0].strip()
                        value = parts[1].strip()
                        data.append((key, value))
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
    return data

def save_data_to_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(f"{item[0]}, {item[1]}\n")
    except IOError:
        print(f"Ошибка при записи в файл {file_path}")