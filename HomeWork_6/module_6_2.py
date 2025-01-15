#Задача "Изменять нельзя получать"
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner:str, __model:str, __color:str,__engine_power:int):
        self.new_color = None
        self.owner = owner
        self.__MODEL = __model
        self.__COLOR = __color
        self.__ENGINE_POWER = __engine_power
        
    def get_model(self):
        print(f'Модель: {self.__MODEL}')
        
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__ENGINE_POWER}')
        
    def get_color(self):
        print(f'Цвет: {self.__COLOR}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color:str):
        self.new_color = new_color
        for color in self.__COLOR_VARIANTS:
            if self.new_color.lower() == color.lower():
                self.__COLOR = self.new_color
        if self.__COLOR != self.new_color:
            print(f'нельзя изменить цвет на {self.new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

#Пример результата выполнения программы:
#Исходный код:
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
print('# Изначальные свойства') # Изначальные свойства
vehicle1.print_info()
print('# Меняем свойства') # Меняем свойства
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print('# Проверяем что поменялось') # Проверяем что поменялось
vehicle1.print_info()