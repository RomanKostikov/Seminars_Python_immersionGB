# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    '''Archive class that holds data of previous archives
    :param num: number value
    :param name: string value

    '''
    _last = []

    def __init__(self, num: int, name: str):
        self.num = num
        self.name = name
        self.archives_list = Archive._last.copy()
        Archive._last.append(self)

    def __repr__(self) -> str:
        return f"Archive({self.num}, '{self.name}')"

    def __str__(self) -> str:
        return f'Arhive of {self.num}, "{self.name}"'


a = Archive(1, 'a')
b = Archive(1, 'b')
c = Archive(1, 'c')
new_a = eval(repr(c))
print(new_a)
print(c)
