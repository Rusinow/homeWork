class Human:

    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Hello, my name is {self.name}, i am {self.age} yars old')

    def birthday(self):
        self.age += 1
        print(f"today my birthday, i'm {self.age} yars old")

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f'{self.name}'

    def __bool__(self):
        return bool(self.age)

    def __del__(self):
        print(f'{self.name} leave')

den = Human('Denis', 22)
maks = Human('Maxim', 22)
a = 6

print(Human.head)