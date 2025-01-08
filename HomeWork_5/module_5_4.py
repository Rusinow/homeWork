class House:

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args[1]

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return  self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __sub__(self, value):
        self.number_of_floors = self.number_of_floors - value
        return self
    def __rsub__(self, value):
        self.number_of_floors = value - self.number_of_floors
        return  self
    def __isub__(self, value):
        self.number_of_floors -= value
        return self

    def __floordiv__(self, value):
        self.number_of_floors = self.number_of_floors // value
        return self
    def __rfloordiv__(self, value):
        self.number_of_floors = value // self.number_of_floors
        return  self
    def __ifloordiv__(self, value):
        self.number_of_floors //= value
        return self

    def go_to(self, new_floor):
        if (new_floor > self.number_of_floors) or (new_floor < 1):
            print('Такого этажа не существует')
        else:
            floor = 1
            while floor <= new_floor:
                print(floor)
                floor += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Назавание: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример результата выполнения программы:
# Пример выполнения программы:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)