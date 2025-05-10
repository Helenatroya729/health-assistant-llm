import json

file_path = "modified_dataset_out_260.jsonl"  # исходный файл
output_file = "dataset_converted260.jsonl"  # файл на выходе

data = []

with open(file_path, "r", encoding="utf-8-sig") as file:
    for line in file:
        entry = json.loads(line.strip())  
        
        # преобразуем поля
        converted_entry = {
            "instruction": entry["prompt"],  # prompt → instruction
            "input": "",  
            "output": entry["completion"]  # completion → output
        }
        
        data.append(converted_entry) 

# сохраняем
with open(output_file, "w", encoding="utf-8") as outfile:
    for entry in data:
        outfile.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Конвертация завершена! Данные сохранены в {output_file}")
