class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other

        return self

    def __iadd__(self, other):
        if isinstance(other, int):
            self.__add__(other)

        return self

    def __radd__(self, other):
        self.__add__(other)

        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # _eq_

h1 = h1 + 10  # _add_
print(h1)
print(h1 == h2)

h1 += 10  # _iadd_
print(h1)

h2 = 10 + h2  # _radd_
print(h2)

print(h1 > h2)  # _gt_
print(h1 >= h2)  # _ge_
print(h1 < h2)  # _lt_
print(h1 <= h2)  # _le_
print(h1 != h2)  # _ne_
