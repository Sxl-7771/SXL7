# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

# Базовый класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

# Класс Mammal наследуется от Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Predator наследуется от Animal
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Flower наследуется от Plant
class Flower(Plant):
    pass

# Класс Fruit наследуется от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создание объектов и тестирование
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка работы
print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False

a1.eat(p1)       # Вывод: Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Вывод: Хатико съел Заводной апельсин

print(a1.alive)  # Вывод: False
print(a2.fed)    # Вывод: True
