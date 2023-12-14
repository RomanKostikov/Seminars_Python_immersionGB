# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.
def get_numeric_input():
    while True:
        try:
            user_input = input("Введите число: ")
            number = float(user_input)
            if number.is_integer():
                number = int(number)
            return number
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")


get_numeric_input()
