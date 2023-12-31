# Урок 4. Функции

## Classwork

### task001:

Задание №1

✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.

### task002:

Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.

### task003:

Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно

### task004:

Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии

### task005:

Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.

### task006:

Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.

### task007:

Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

### task008:

Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

## Homework

### task001:

Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
и возвращает транспонированную матрицу.

### task002:

Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

### task003:

У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:

Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. Пополнение 
счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:

Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна 
быть кратной MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, 
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:

Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM, 
начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:

Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY. 
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.