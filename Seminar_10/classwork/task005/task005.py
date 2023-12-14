# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def info(self):
        print(f"I am a fish named {self.name}. I live in {self.habitat}.")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def info(self):
        print(f"I am a bird named {self.name}. My wingspan is {self.wingspan}.")


class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def info(self):
        print(f"I am a mammal named {self.name}. I make {self.sound}.")


fish = Fish("Nemo", "the ocean")
bird = Bird("Tweety", "30cm")
mammal = Mammal("Simba", "roaring")

fish.info()
bird.info()
mammal.info()
