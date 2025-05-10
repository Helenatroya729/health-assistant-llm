import json

file_path = "combined_dataset.jsonl"
data = []

with open(file_path, "r", encoding="utf-8-sig") as file: 
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  # убираем лишние пробелы и переносы строк
        if not line:  # игнорируем пустые строки
            continue
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Ошибка в строке {line_number}: {e}")
            print(f"Строка: {line}")

# Проверка структуры данных (первый элемент)
if data:
    print("Пример данных (первый элемент):", data[0])

# Получим все ключи из первого объекта
if data:
    keys = data[0].keys()
    print("Ключи данных:", keys)
    
    
Вывод: 
Пример данных (первый элемент): {'prompt': 'Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++, Trait: protein.', 'completion': 'Сбалансированно: Генетический анализ выявил у вас низкую потребность в соблюдении белковой диеты для сохранения физической формы.'}
Ключи данных: dict_keys(['prompt', 'completion'])