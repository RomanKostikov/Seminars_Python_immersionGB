# Задание №6
# Доработайте предыдущую задачу.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.
class Animal:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_spec_info(self):
        print(self.name, self.age, sep="\t")


class Bird(Animal):
    wings_width: float
    flight_height: float

    def __init__(self, name, age, wings_width, flight_height):
        super().__init__(name, age)
        self.wings_width = wings_width
        self.flight_height = flight_height

    def print_spec_info(self):
        print(self.wings_width, self.flight_height, sep="\t")


class Fish(Animal):
    length: float
    dive_depth: float

    def __init__(self, name, age, length, dive_depth):
        super().__init__(name, age)
        self.length = length
        self.dive_depth = dive_depth

    def print_spec_info(self):
        print(self.length, self.dive_depth, sep="\t")


class Mammal(Animal):
    paws_count: int
    jump_height: float

    def __init__(self, name, age, paws_count, jump_height):
        super().__init__(name, age)
        self.paws_count = paws_count
        self.jump_height = jump_height

    def print_spec_info(self):
        print(self.paws_count, self.jump_height, sep="\t")


animal1 = Animal('Animal', 1)
chicken = Bird('Chicken', 1, 25.5, 0)
cod = Fish('Cod', 0, 5, 20)
cat = Mammal('Cat', 5, 4, 200)

animal1.print_spec_info()
chicken.print_spec_info()
cod.print_spec_info()
cat.print_spec_info()
print(cat.name)
