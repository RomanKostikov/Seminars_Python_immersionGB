# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку

print('\n\n'.join(
    ['\n'.join(['\t\t'.join([f'{y} x {x} = {x * y:>2}' for y in range(2 + k, 6 + k)]) for x in range(2, 10)]) for k in
     [0, 4]]))
