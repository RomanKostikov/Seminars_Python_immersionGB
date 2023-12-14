# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
# считать двумя словами.
# Цифры за слова не считаем. Отсортируйте по убыванию значения количества повторяющихся слов.
# На входе:
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
def count_words(text):
    # Удаляем знаки препинания и регистр символов
    text = ''.join(c.lower() if c.isalpha() or c == ' ' else ' ' for c in text)
    # Разделяем текст на слова
    words = text.split()
    # Создаем словарь для подсчета количества каждого слова
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # Сортируем словарь по убыванию количества повторений и возвращаем 10 самых частых слов
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts[:10]


text = 'Hello world. Hello Python 3.9. Hello again.'
result = count_words(text)
print(result)
