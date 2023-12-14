# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.
text = "Hello, world!"

# Step 2: Create a dictionary where the key is a letter and the value is its code
letter_code_dict = {letter: ord(letter) for letter in text}
# Step 1: Save the dictionary iterator
iterator = iter(letter_code_dict.items())

# Step 2: Print the first 5 key-value pairs using the iterator
for i in range(5):
    key, value = next(iterator)
    print(f"{key}: {value}")
