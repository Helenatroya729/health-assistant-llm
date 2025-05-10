from datasets import load_dataset
import requests


alpaca_prompt = """Вам дана инструкция, на основе которой нужно предоставить рекомендации:

### Инструкция:
{}

### Вводные данные:
{}

### Ответ:
{}"""


EOS_TOKEN = tokenizer.eos_token  

# форматирование данных
def formatting_prompts_func(examples):
    instructions = examples["instruction"]
    inputs = examples["input"]
    outputs = examples["output"]
    
    texts = []
    for instruction, input, output in zip(instructions, inputs, outputs):
        # добавляем EOS_TOKEN
        text = alpaca_prompt.format(instruction, input, output) + EOS_TOKEN
        texts.append(text)
    
    return {"text": texts}

# загружаем локальный датасет
dataset = load_dataset("json", data_files="dataset_converted260.jsonl", split="train")


dataset = dataset.map(formatting_prompts_func, batched=True)