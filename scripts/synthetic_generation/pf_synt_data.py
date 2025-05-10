import json
from ollama import Client
import time

# подключаемся к Ollama
client = Client(host='http://localhost:11434')

input_file = "modified_dataset.jsonl"
output_file = "modified_dataset_out.jsonl"

new_entries = []



with open(input_file, "r", encoding="utf-8-sig") as infile:
    lines = infile.readlines()


with open(output_file, "a", encoding="utf-8") as outfile:
    for index, line in enumerate(lines, start=1):
        try:
            data = json.loads(line.strip())

            if data["Var"] < 32 and len(data["completion"]) < 300:
                original_text = data["completion"]
                print(f"Строка {index}: Обрабатываем строку: {data['prompt']}")
                print(f"\nСодержимое completion: {original_text}")
                
                prompt = f"Перепиши этот текст, используя перефразирование: \"{original_text}\""
                
                

                response = client.chat(
                    model="llama3.1",
                    messages=[{"role": "user", "content": prompt}]
                )

                paraphrased_text = response["message"]["content"]
                print(f"\nСгенерированное значение: {paraphrased_text}\n")

                new_entry = {
                    "prompt": data["prompt"],
                    "completion": paraphrased_text,
                    "Type": "S",
                    "Var": 30
                }
                
 
                outfile.write(json.dumps(new_entry, ensure_ascii=False) + "\n")
                

                data["Var"] += 1


            outfile.write(json.dumps(data, ensure_ascii=False) + "\n")

        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e} в строке: {line}")


for entry in new_entries:
    print(json.dumps(entry, ensure_ascii=False, indent=4))
