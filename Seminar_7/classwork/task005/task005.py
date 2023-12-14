# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import randint, choices, randbytes
from string import ascii_letters


def create_filename(min_len: int = 6, max_len: int = 30) -> str:
    filename_len = randint(min_len, max_len)

    return ''.join(choices(ascii_letters, k=filename_len))


def create_inner_file(min_bytes: int = 256, max_bytes: int = 4096):
    file_bytes = randint(min_bytes, max_bytes)

    return randbytes(file_bytes)


def create_files(files_ext: str = 'txt', files_count=42, min_len=6, max_len=30,
                 min_bytes=256, max_bytes=4096):
    for _ in range(files_count):
        with open('.'.join((create_filename(min_len, max_len), files_ext)), 'wb') as f:
            f.write(create_inner_file(min_bytes, max_bytes))


def create_files_with_variable_exts(files_with_exts: dict[str, int], ):
    for file_ext, files_cnt in files_with_exts.items():
        create_files(file_ext, files_cnt)


# create_files('12', 5)
create_files_with_variable_exts({
    'txt': 10,
    '12': 2,
    'ini': 5
})
