# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def get_unicode_codes(text):
    unique_codes = sorted(set(ord(char) for char in text), reverse=True)
    return unique_codes


def main():
    text = "Это пример текста, который будет обработан функцией print_words"
    unicode_codes = get_unicode_codes(text)
    print(unicode_codes)


if __name__ == "__main__":
    main()
