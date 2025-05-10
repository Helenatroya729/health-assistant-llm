import json

file_path = "combined_dataset.jsonl"
data = []

with open(file_path, "r", encoding="utf-8-sig") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()  # убираем лишние пробелы и переносы строк
        if not line:  # игнорируем пустые строки
            continue
        try:
            # парсим строку
            json_data = json.loads(line)
            
            # извлекаем текст после маркера ### completion: из prompt
            prompt = json_data.get("prompt", "")
            completion_marker = "### completion:"
            if completion_marker in prompt:
                prompt_parts = prompt.split(completion_marker)
                question = prompt_parts[1].strip()
                prompt_without_completion = prompt_parts[0].strip()
                
                # модифицируем поле completion
                original_completion = json_data.get("completion", "")
                modified_completion = f"Вопрос: {question} Ответ: {original_completion}"
                
                # обновляем поля в JSON
                json_data["prompt"] = prompt_without_completion
                json_data["completion"] = modified_completion
            
            data.append(json_data)
        except json.JSONDecodeError as e:  # выводим информацию если есть ошибки
            print(f"Ошибка в строке {line_number}: {e}")
            print(f"Строка: {line}")

if data:
    print("Начало набора данных:")
    print(json.dumps(data[:3], ensure_ascii=False, indent=4))


if data:
    print("\nОкончание набора данных:")
    print(json.dumps(data[-3:], ensure_ascii=False, indent=4))
    
    
Вывод:
Начало набора данных:
[
    {
        "prompt": "Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++, Trait: protein.",
        "completion": "Сбалансированно: Генетический анализ выявил у вас низкую потребность в соблюдении белковой диеты для сохранения физической формы."
    },
    {
        "prompt": "Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++, Category: Пищевое поведение.",
        "completion": "Генетически вы не склонны к перееданию. Поэтому количество белков в рационе рекомендуется поддерживать в пределах физиологической потребности. Суточная норма потребления белков может составлять от 0,8 до 1,5 г/кг идеальной массы тела, т.е. примерно 10–15% от общей суточной калорийности рациона. При занятиях спортом количество белка может быть увеличено до 2,5 г на килограмм массы тела (20–25%)*. Это необходимо для восстановления разрушенных в процессе тренировки клеток. Потребление белков ускоряет метаболизм, что немаловажно при наборе мышечной массы, а также для контроля веса*."
    },
    {
        "prompt": "Профиль: Gen: FTO, Polymorphism: rs9939609, Variant: TT, Effect: ++.",
        "completion": "При высокоинтенсивных тренировках после консультации специалиста возможен дополнительный прием спортивного питания (протеинов) и аминокислот (ВСАА)*. При постоянной высокобелковой диете рекомендованы консультации врача, регулярные анализы крови (общий, биохимия) и обследования почек и печени (показатели АЛТ, АСТ и билирубина в биохимическом анализе крови, общий анализ мочи, УЗИ печени и почек и другие дополнительные обследования по назначению специалиста)*."
    }
]

Окончание набора данных:
[
    {
        "prompt": "Профиль: Gen: HTR2A, Polymorphism: rs6311, Variant: CC, Effect: ++, Gen: SLC6A4, Polymorphism: rs25531, Variant: LL, Effect: 0+, Gen: OXTR, Polymorphism: rs53576, Variant: GG, Effect: --, Gen: GRIN2B, Polymorphism: rs1806201, Variant: TT, Effect: +-, Gen: BDNF, Polymorphism: rs6265, Variant: CC, Effect: 0.",
        "completion": "Вопрос: Могу ли я заниматься шахматами как хобби? Ответ: Шахматы подойдут как хобби, занимайтесь 2–3 часа в неделю. На перекус ешьте 30 г орехов с яблоком."
    },
    {
        "prompt": "Профиль: Gen: LEPR, Polymorphism: rs1137101, Variant: AA, Effect: ++, Gen: POMC, Polymorphism: rs1042571, Variant: GG, Effect: --, Gen: FTO, Polymorphism: rs1421085, Variant: TT, Effect: --, Gen: MC4R, Polymorphism: rs17782313, Variant: TT, Effect: ++, Gen: ADRB2, Polymorphism: rs1042714, Variant: CC, Effect: ++.",
        "completion": "Вопрос: Как справляться с жарой летом? Ответ: В жару пейте 2–3 л воды в день и ешьте лёгкие блюда: 100 г рыбы с овощами 2 раза в день."
    },
    {
        "prompt": "Профиль: Gen: TCF7L2, Polymorphism: rs7903146, Variant: TT, Effect: --, Gen: GIPR, Polymorphism: rs2287019, Variant: CC, Effect: ++, Gen: INSIG2, Polymorphism: rs7566605, Variant: GG, Effect: --, Gen: ADRB1, Polymorphism: rs1801253, Variant: GG, Effect: 0+, Gen: PPARG, Polymorphism: rs1801282, Variant: CG, Effect: +-.",
        "completion": "Вопрос: Стоит ли мне пить протеин после прогулки? Ответ: Протеин (200 мл) можно пить после прогулки длительностью более часа. В ином случае ешьте 100 г курицы."
    }
]