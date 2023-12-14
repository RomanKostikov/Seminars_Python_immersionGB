# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def create_json_from_txt(src_filename: str = 'result.txt',
                         res_filename: str = 'result.json'):
    with open(os.path.join(BASE_DIR, src_filename), 'r', encoding='utf-8') as f:
        file_lines = [el.split(' | ') for el in f.readlines()]

    file_lines = list(map(lambda x: (x[0].title(), float(x[1])), file_lines))

    names_dict = dict(file_lines)

    with open(os.path.join(BASE_DIR, res_filename), 'w', encoding='utf-8') as f:
        json.dump(names_dict, f, indent=2, ensure_ascii=False)


create_json_from_txt()
