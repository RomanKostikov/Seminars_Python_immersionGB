# Задание №1
#
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки


def f(text):
    text_list = sorted(text.lower().split())
    max_len_word = max(text_list, key=len)
    length = len(max_len_word)
    for i, word in enumerate(text_list, 1):
        print(i, f"{word:>{length}}")


def main():
    text = "Это пример текста, который будет обработан функцией print_words"
    f(text)


if __name__ == "__main__":
    main()
