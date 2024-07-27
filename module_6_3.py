# Класс Horse - описывает лошадь
class Horse:
    def __init__(self):
        # Инициализация атрибутов для объекта лошади
        self.x_distance = 0  # начальная горизонтальная позиция
        self.sound = 'Frrr'  # звук, издаваемый лошадью

    # Метод для перемещения лошади
    def run(self, dx):
        """
        Увеличивает пройденный путь по горизонтали на значение dx.
        :param dx: изменение пройденного пути
        """
        self.x_distance += dx  # изменяем x_distance на dx

# Класс Eagle - описывает орла
class Eagle:
    def __init__(self):
        # Инициализация атрибутов для объекта орла
        self.y_distance = 0  # начальная высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # звук, издаваемый орлом

    # Метод для перемещения орла
    def fly(self, dy):
        """
        Увеличивает высоту полета на значение dy.
        :param dy: изменение высоты полета
        """
        self.y_distance += dy  # изменяем y_distance на dy

# Класс Pegasus - описывает пегаса, наследуется от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        # Вызов конструкторов родительских классов
        Horse.__init__(self)  # Инициализируем атрибуты Horse
        Eagle.__init__(self)  # Инициализируем атрибуты Eagle

    # Метод для перемещения пегаса
    def move(self, dx, dy):
        """
        Перемещает пегаса на dx по горизонтали и на dy по вертикали.
        :param dx: изменение пройденного пути
        :param dy: изменение высоты полета
        """
        self.run(dx)  # используем метод run из Horse
        self.fly(dy)  # используем метод fly из Eagle

    # Метод для получения текущей позиции пегаса
    def get_pos(self):
        """
        Возвращает текущее положение пегаса.
        :return: кортеж (x_distance, y_distance)
        """
        return self.x_distance, self.y_distance

    # Метод для получения звука пегаса
    def voice(self):
        """
        Выводит звук, который издает пегас.
        """
        print(self.sound)  # из-за MRO, sound берется из Eagle

# Пример работы программы
if __name__ == "__main__":
    # Создаем объект класса Pegasus
    p1 = Pegasus()

    # Получаем начальное положение пегаса
    print(p1.get_pos())  # ожидаем (0, 0)

    # Перемещаем пегаса на (10, 15)
    p1.move(10, 15)
    print(p1.get_pos())  # ожидаем (10, 15)

    # Перемещаем пегаса на (-5, 20)
    p1.move(-5, 20)
    print(p1.get_pos())  # ожидаем (5, 35)

    # Получаем звук, который издает пегас
    p1.voice()  # ожидаем "I train, eat, sleep, and repeat"
