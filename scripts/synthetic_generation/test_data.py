import json

file_path = "deduplicated_dataset.jsonl"
data = []

with open(file_path, "r", encoding="utf-8-sig") as file: 
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  # убираем лишние пробелы и переносы строк
        if not line:  
            continue
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Ошибка в строке {line_number}: {e}")
            print(f"Строка: {line}")


required_keys = ['prompt', 'completion']  

# Проверка на пропущенные значения
missing_values = {key: [] for key in required_keys}

for idx, entry in enumerate(data):
    for key in required_keys:
        if key not in entry or entry[key] is None:
            missing_values[key].append(idx)

for key, indices in missing_values.items():
    if indices:
        print(f"Отсутствуют значения для ключа '{key}' в строках: {indices}")
    
    
missing_keys = [item for item in data if "prompt" not in item or "completion" not in item]
print(f"Ошибок в структуре записей: {len(missing_keys)}")


Вывод:
Ошибок в структуре записей: 0