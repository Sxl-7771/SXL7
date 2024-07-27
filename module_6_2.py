# Класс Vehicle - базовый класс для любого транспорта
class Vehicle:
    # Атрибут класса: допустимые цвета
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    # Конструктор класса
    def __init__(self, owner, model, color, engine_power):
        # Атрибуты объекта
        self.owner = owner  # Владелец транспорта
        self.__model = model  # Модель транспорта, скрыта от изменения
        self.__engine_power = engine_power  # Мощность двигателя, скрыта от изменения
        self.__color = color  # Цвет, скрыт от изменения

    # Метод для получения модели транспорта
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета транспорта
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод для изменения цвета транспорта, если он в списке допустимых
    def set_color(self, new_color):
        # Проверяем, есть ли новый цвет в списке допустимых (без учета регистра)
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color  # Устанавливаем новый цвет
        else:
            # Сообщаем, что цвет не может быть изменен
            print(f"Нельзя сменить цвет на {new_color}")

    # Метод для печати информации о транспорте
    def print_info(self):
        # Вывод информации в заданном формате
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


# Класс Sedan - наследник Vehicle
class Sedan(Vehicle):
    # Атрибут класса: максимальное количество пассажиров
    __PASSENGERS_LIMIT = 5

    # Конструктор принимает те же параметры, что и Vehicle
    def __init__(self, owner, model, color, engine_power):
        # Вызов конструктора базового класса Vehicle
        super().__init__(owner, model, color, engine_power)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')  # Нельзя сменить цвет на Pink
vehicle1.set_color('BLACK')  # Цвет изменится
vehicle1.owner = 'Vasyok'  # Изменение владельца

# Проверяем что поменялось
vehicle1.print_info()
