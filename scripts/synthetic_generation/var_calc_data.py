import json

file_path = "modified_dataset.jsonl"


data = []
missing_variations = {}
TARGET_COUNT = 30  # базовое количество вариаций

with open(file_path, "r", encoding="utf-8-sig") as file:
    for line in file:
        entry = json.loads(line.strip())
        data.append(entry)
        val = entry.get("Var", 0)  # используем значение Val датасета
        missing_count = max(0, TARGET_COUNT - val)
        missing_variations[entry["prompt"]] = missing_count

# вывод первых 10 значений для проверки
for prompt, missing in list(missing_variations.items())[:10]:
    print(f"Prompt: {prompt}\nНедостающих вариаций: {missing}\n")
    
    
Вывод:
Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++, Trait: protein.
Недостающих вариаций: 28

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++, Category: Пищевое поведение.
Недостающих вариаций: 8

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++.
Недостающих вариаций: 8

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TA, Effect: +-, Trait: protein.
Недостающих вариаций: 27

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TA, Effect: +-, Category: Пищевое поведение.
Недостающих вариаций: 9

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TA, Effect: +-.
Недостающих вариаций: 9

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: AA, Effect: --, Trait: protein.
Недостающих вариаций: 28

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: AA, Effect: --, Category: Пищевое поведение.
Недостающих вариаций: 8

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: AA, Effect: --.
Недостающих вариаций: 8

Prompt: Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: --, Trait: protein.
Недостающих вариаций: 29