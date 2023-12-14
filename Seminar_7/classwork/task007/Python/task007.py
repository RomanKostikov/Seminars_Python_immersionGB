# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
# Спасибо, до свидания.
import os


def sort_files(exts_dict: dict[str, list[str]]):
    for file_name in os.listdir():
        if os.path.isfile(file_name):
            for directory, files_exts in exts_dict.items():
                if file_name.split('.')[-1] in files_exts:
                    if not os.path.isdir(directory):
                        os.mkdir(directory)

                    os.replace(file_name, os.path.join(directory, file_name))


sort_files({'Python': ['py', 'pyc'],
            'Movies': ['avi', 'mp4']})
