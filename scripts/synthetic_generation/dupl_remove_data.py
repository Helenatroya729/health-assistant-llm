import json

input_file = "modified_dataset_out.jsonl"
output_file = "deduplicated_dataset.jsonl"

unique_entries = set()
deduplicated_lines = []

total_lines = sum(1 for _ in open(input_file, "r", encoding="utf-8"))
processed_lines = 0

# читаем входной файл
with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        try:
            data = json.loads(line.strip())
            entry_key = (data["prompt"], data["completion"])  
            
            if entry_key not in unique_entries:
                unique_entries.add(entry_key)
                deduplicated_lines.append(line)
            
            processed_lines += 1
            if processed_lines % 100 == 0 or processed_lines == total_lines:
                print(f"Обработано {processed_lines} из {total_lines} строк...")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e} в строке: {line}")

# записываем очищенные данные в новый файл
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(deduplicated_lines)

print(f"Удалены дубликаты. Итоговый файл: {output_file}")