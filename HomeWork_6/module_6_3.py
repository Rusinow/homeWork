#Задача "Ошибка эволюции":
from random import randint

class Animal:
    def __init__(self, speed:int):
        self.speed = speed
    live = True
    sound = None
    _cords = [0, 0, 0]
    _DEGREE_OF_DANGER = 0

    def  move(self, dx:int, dy:int, dz:int):
        self._cords[0] = int(dx*self.speed)
        self._cords[1] = int(dy*self.speed)
        self._cords[2] = int(dz*self.speed)

    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    brek = True

    def lay_eggs(self):
        print(f'Here are(is) {randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = int(abs(dz)*self.speed/2)

class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
    sound = "Click-click-click"

# Пример работы программы:
db = Duckbill(10)
print(db.live)
print(db.brek)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(-5)
db.get_cords()
db.lay_eggs()