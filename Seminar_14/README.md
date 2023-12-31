# Урок 14. Основы тестирования

## Classwork

### task001:

Задание №1
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.

### task002:

Задание №2
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)

### task003:

Задание №3
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)

### task004:

Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)

### task005:

Задание №5
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.

### task006:

Задание №6
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.

## Homework

### task001:

Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Используйте модуль doctest.
Тесты:
test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной 
шириной (-2). Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError.
test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4. 
Проверяем, что r2.width равно 3 и r2.height равно 4.
test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.
perimeter() возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() 
возвращает 14.
test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() 
возвращает 25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.
test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. 
Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и 
высоты (8 и 6.0 соответственно).
test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4. 
Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины 
и высоты (2 и 2.0 соответственно).
Запускать тесты не надо, автотест это сделает сам:

### task002:

Rectangle тесты unittest
Инструкция по использованию платформы
Возьмите код из прошлой задачи "Класс Rectangle".
Напишите к ней тесты, используя unittest и лежать в class TestRectangle(unittest.TestCase)
Тесты:
test_width: Тестирование инициализации ширины. Создайте прямоугольник с шириной 5 и убедитесь, что атрибут width
корректно установлен на 5.
test_height: Тестирование инициализации ширины и высоты. Создайте прямоугольник с шириной 3 и высотой 4 и убедитесь,
что атрибут height корректно установлен на 4.
test_perimeter: Тестирование вычисления периметра. Создайте прямоугольник с шириной 5 и вычислите его периметр.
Убедитесь, что результат равен 20.
test_area: Тестирование вычисления площади. Создайте прямоугольник с шириной 3 и высотой 4 и вычислите его площадь. 
Убедитесь, что результат равен 12.
test_addition: Тестирование операции сложения. Создайте два прямоугольника: один с шириной 5, другой с шириной 3 и 
высотой 4. Выполните операцию сложения r1 + r2 и убедитесь, что полученный прямоугольник имеет правильные значения 
ширины и высоты (8 и 6.0 соответственно).
test_subtraction: Тестирование операции вычитания. Создайте два прямоугольника: один с шириной 10, другой с шириной 3 и 
высотой 4. Выполните операцию вычитания r1 - r2 и убедитесь, что полученный прямоугольник имеет правильные значения 
ширины и высоты (7 и 6.0 соответственно).
test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать прямоугольник с отрицательной
шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.
test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать прямоугольник с шириной 5 и 
отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.
test_set_width: Тестирование изменения ширины. Создайте прямоугольник с шириной 5 и измените его ширину на 10. 
Убедитесь, что атрибут width корректно изменяется на 10.
test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте прямоугольник с шириной 5 и 
попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь, что это вызывает исключение 
NegativeValueError.
test_set_height: Тестирование изменения высоты. Создайте прямоугольник с шириной 3 и высотой 4 и измените 
его высоту на 6. Убедитесь, что атрибут height корректно изменяется на 6.
test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте прямоугольник с шириной 3 и 
высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6). Убедитесь, что это вызывает 
исключение NegativeValueError.
test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. Создайте 
два прямоугольника: один с шириной 3 и высотой 4, другой с шириной 10. Попробуйте выполнить операцию 
вычитания r1 - r2 и убедитесь, что это вызывает исключение NegativeValueError.
test_subtraction_same_perimeter: Тестирование операции вычитания с прямоугольниками одинакового периметра. 
Создайте два прямоугольника: один с шириной 5, другой с шириной 4 и высотой 3. Выполните операцию вычитания r1 - r2 
и убедитесь, что полученный прямоугольник имеет правильные значения ширины и высоты (1 и 1.0 соответственно).
Используйте модуль unittest для запуска тестов. Все тесты должны выполняться успешно и не вызывать ошибок.
Запускать тесты не надо, автотест это сделает сам:

### task003:
Управление информацией о сотрудниках и их возрасте doctest
Инструкция по использованию платформы
Возьмите код из прошлой задачи "Управление информацией о сотрудниках и их возрасте".
Ваша задача - написать набор тестов для класса Employee с использованием модуля doctest, 
чтобы убедиться, что он работает правильно.
Тесты:
test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", 
именем "Ivan", отчеством "Ivanovich" и возрастом 30. Убедитесь, что метод full_name() возвращает правильное 
полное имя в формате "Ivanov Ivan Ivanovich".
test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", 
отчеством "Ivanovich" и возрастом 30. Вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и 
стал равным 31.
test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с фамилией "Ivanov", 
именем "Ivan", отчеством "Ivanovich", возрастом 30, должностью "manager" и зарплатой 50000. Вызовите метод 
raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.
test_employee_str: Тестирование метода __str__(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", 
отчеством "Ivanovich", возрастом 30, должностью "manager" и зарплатой 50000. Убедитесь, что метод __str__() 
возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".
test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "ivanov" (в 
нижнем регистре), именем "ivan" (в нижнем регистре), отчеством "ivanovich" (в нижнем регистре), возрастом 30, 
должностью "manager" и зарплатой 50000. Убедитесь, что атрибут last_name возвращается в верхнем регистре, 
то есть "Ivanov".
Запускать тесты не надо, автотест это сделает сам:

### task004:
Класс Rectangle - работа с прямоугольниками Pytest
Инструкция по использованию платформы
Вам предоставлен код на Python из предыдущих задач, который содержит два класса: Rectangle и NegativeValueError.
Ваша задача - написать набор тестов для класса Rectangle, чтобы убедиться, что он работает правильно и обрабатывает 
некорректные значения.
Тесты должны быть написаны с использованием модуля pytest.
*Тесты необходимо написать именно в этом порядке!
Тесты:
test_width: Тестирование инициализации ширины. Создайте объект Rectangle с шириной 5 и убедитесь, что ширина 
установлена правильно.
test_height: Тестирование инициализации ширины и высоты. Создайте объект Rectangle с шириной 3 и высотой 4 и 
убедитесь, что высота установлена правильно.
test_perimeter: Тестирование вычисления периметра. Создайте объект Rectangle с шириной 5 и вычислите его периметр 
(должен быть равен 20).
test_area: Тестирование вычисления площади. Создайте объект Rectangle с шириной 3 и высотой 4 и вычислите его 
площадь (должна быть равна 12).
test_addition: Тестирование операции сложения двух прямоугольников. Создайте два объекта Rectangle с ширинами
5 и 3, и высотами 1 и 4 соответственно. Произведите операцию сложения и убедитесь, что полученный прямоугольник 
имеет правильные значения ширины и высоты.
test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать объект Rectangle с 
отрицательной шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.
test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать объект Rectangle с 
шириной 5 и отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.
test_set_width: Тестирование изменения ширины. Создайте объект Rectangle с шириной 5 и измените его ширину на 10. 
Убедитесь, что ширина изменена правильно.
test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте объект Rectangle с шириной 5 и 
попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь, что это вызывает исключение
NegativeValueError.
test_set_height: Тестирование изменения высоты. Создайте объект Rectangle с шириной 3 и высотой 4 и измените его 
высоту на 6. Убедитесь, что высота изменена правильно.
test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте объект Rectangle с шириной 3 и 
высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6). Убедитесь, что это вызывает исключение 
NegativeValueError.
test_subtraction: Тестирование операции вычитания двух прямоугольников. Создайте два объекта Rectangle с ширинами 
10 и 3, и высотами 1 и 4 соответственно. Произведите операцию вычитания и убедитесь, что полученный прямоугольник 
имеет правильные значения ширины и высоты.
test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. Создайте два объекта 
Rectangle с ширинами 3 и 10, и высотами 4 и 1 соответственно. Попробуйте выполнить операцию вычитания и убедитесь, 
что это вызывает исключение NegativeValueError.
test_subtraction_same_perimeter: Тестирование операции вычитания с одинаковым периметром. Создайте два объекта
Rectangle с ширинами 5 и 4, и высотами 1 и 3 соответственно. Произведите операцию вычитания и убедитесь, что полученный 
прямоугольник имеет правильные значения ширины и высоты.
Запускать тесты не надо, автотест это сделает сам:

### task005:

Класс Rectangle - работа с прямоугольниками Pytest
Инструкция по использованию платформы
Вам предоставлен код на Python из предыдущих задач, который содержит два класса: Rectangle и NegativeValueError.
Ваша задача - написать набор тестов для класса Rectangle, чтобы убедиться, что он работает правильно и о
брабатывает некорректные значения.
Тесты должны быть написаны с использованием модуля pytest.
*Тесты необходимо написать именно в этом порядке!
Тесты:
test_width: Тестирование инициализации ширины. Создайте объект Rectangle с шириной 5 и убедитесь, что
ширина установлена правильно.
test_height: Тестирование инициализации ширины и высоты. Создайте объект Rectangle с шириной 3 и высотой 
4 и убедитесь, что высота установлена правильно.
test_perimeter: Тестирование вычисления периметра. Создайте объект Rectangle с шириной 5 и вычислите его 
периметр (должен быть равен 20).
test_area: Тестирование вычисления площади. Создайте объект Rectangle с шириной 3 и высотой 4 и вычислите его
площадь (должна быть равна 12).
test_addition: Тестирование операции сложения двух прямоугольников. Создайте два объекта Rectangle с ширинами 
5 и 3, и высотами 1 и 4 соответственно. Произведите операцию сложения и убедитесь, что полученный 
прямоугольник имеет правильные значения ширины и высоты.
test_negative_width: Тестирование инициализации отрицательной ширины. Попробуйте создать объект Rectangle с 
отрицательной шириной (-5) и убедитесь, что это вызывает исключение NegativeValueError.
test_negative_height: Тестирование инициализации отрицательной высоты. Попробуйте создать объект Rectangle с
шириной 5 и отрицательной высотой (-4) и убедитесь, что это вызывает исключение NegativeValueError.
test_set_width: Тестирование изменения ширины. Создайте объект Rectangle с шириной 5 и измените его ширину на 10. 
Убедитесь, что ширина изменена правильно.
test_set_negative_width: Тестирование изменения отрицательной ширины. Создайте объект Rectangle с шириной 5 и
попробуйте изменить его ширину на отрицательное значение (-10). Убедитесь, что это вызывает исключение
NegativeValueError.
test_set_height: Тестирование изменения высоты. Создайте объект Rectangle с шириной 3 и высотой 4 и измените его 
высоту на 6. Убедитесь, что высота изменена правильно.
test_set_negative_height: Тестирование изменения отрицательной высоты. Создайте объект Rectangle с шириной 3 и 
высотой 4 и попробуйте изменить его высоту на отрицательное значение (-6). Убедитесь, что это вызывает исключение 
NegativeValueError.
test_subtraction: Тестирование операции вычитания двух прямоугольников. Создайте два объекта Rectangle с 
ширинами 10 и 3, и высотами 1 и 4 соответственно. Произведите операцию вычитания и убедитесь, что полученный 
прямоугольник имеет правильные значения ширины и высоты.
test_subtraction_negative_result: Тестирование операции вычитания с отрицательным результатом. 
Создайте два объекта Rectangle с ширинами 3 и 10, и высотами 4 и 1 соответственно. Попробуйте 
выполнить операцию вычитания и убедитесь, что это вызывает исключение NegativeValueError.
test_subtraction_same_perimeter: Тестирование операции вычитания с одинаковым периметром. Создайте два объекта 
Rectangle с ширинами 5 и 4, и высотами 1 и 3 соответственно. Произведите операцию вычитания и убедитесь, 
что полученный прямоугольник имеет правильные значения ширины и высоты.
Запускать тесты не надо, автотест это сделает сам:

### task006:
Управление информацией о сотрудниках и их возрасте pytest
Инструкция по использованию платформы
У вас есть два класса: Person и Employee из предыдущих задач.
Необходимо написать тесты с использованием модуля pytest и лежать в class TestEmployee.
*Тесты необходимо написать именно в этом порядке!
Тесты:
test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", именем 
"Ivan", отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя в формате 
"Ivanov Ivan Ivanovich".
test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, вызовите
метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.
test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000, 
вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.
test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", имя "Ivan", 
отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод __str__() возвращает 
правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".
test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и 
убедитесь, что атрибут last_nameвозвращается в верхнем регистре, то есть "Ivanov".
Запускать тесты не надо, автотест это сделает сам: