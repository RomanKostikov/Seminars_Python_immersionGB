# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

letters = 'numbers'
words = 'bananas fgdfg dfgdf s'
text = 'cherry gdsfd'
s = 'latter s'


def replace_s_variables():
    variables = [var for var in globals() if var.endswith('s') and var != 's']
    for var in variables:
        new_var = var[:-1]
        globals()[new_var] = globals()[var]
        globals()[var] = None


replace_s_variables()
print(letters, words, text, s)
