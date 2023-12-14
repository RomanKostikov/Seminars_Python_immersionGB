# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку
# Step 1: Save the text as a string
text = "Hello, world!"

# Step 2: Create a dictionary where the key is a letter and the value is its code
letter_code_dict = {letter: ord(letter) for letter in text}

# Step 3: Convert the dictionary into a single string
result = ', '.join(f'{k}: {v}' for k, v in letter_code_dict.items())

print(result)
