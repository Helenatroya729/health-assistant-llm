import json
from collections import Counter

file_path = "modified_dataset.jsonl"
data = []
prompt_counts = Counter()

# читаем JSONL и считаем количество повторений prompt
with open(file_path, "r", encoding="utf-8-sig") as file:
    for line in file:
        json_data = json.loads(line.strip())
        prompt = json_data.get("prompt", "")
        prompt_counts[prompt] += 1
        data.append(json_data)

# записываем в var количество дубликатов
for json_data in data:
    prompt = json_data.get("prompt", "")
    json_data["Var"] = prompt_counts[prompt]


with open(file_path, "w", encoding="utf-8-sig") as output_file:
    for item in data:
        output_file.write(json.dumps(item, ensure_ascii=False) + "\n")

var_values = list(prompt_counts.values())
if var_values:
    print(f"Минимальное значение Var: {min(var_values)}")
    print(f"Максимальное значение Var: {max(var_values)}")
    
print("Обновление завершено. Дубликаты внесены в поле Var.")



Вывод:
Минимальное значение Var: 1
Максимальное значение Var: 30
Обновление завершено. Дубликаты внесены в поле Var.