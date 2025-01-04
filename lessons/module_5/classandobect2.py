class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Hello, my name is {self.name}, i am {self.age} yars old')

    def birthday(self):
        self.age += 1
        print(f"today my birthday, i'm {self.age} yars old")




den = Human('Denis', 22)
max = Human('Maxim', 24)

max.birthday()