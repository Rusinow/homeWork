#Задача "Ошибка эволюции":
from random import randint
class Animal:                                 #Класс описывающий животных
    def __init__(self, speed, _cords = [0, 0, 0], _DEGREE_OF_DANGER = 0):
        super().__init__().speed = speed
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def  move(self, dx, dy, dz):
        pass

class Bird(Animal):                           #Класс описывающий птиц. Наследуется от Animal
    def __init__(self, brek = True):
        super().__init__(brek)
        self.brek = brek

    def lay_eggs(self):
        print(f'Here are(is) {randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    pass

class PoisonousAnimal(Animal):
    pass

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed, brek):
        self.speed = speed
        super().__init__(brek)
    sound = "Click-click-click"

# Пример результата выполнения программы:
# Пример работы программы:
db = Duckbill(10)
print(db.live)
print(db.beak)
# db.speak()
# db.attack()
# db.move(1, 2, 3)
# db.get_cords()
# db.dive_in(6)
# db.get_cords()
# db.lay_eggs()