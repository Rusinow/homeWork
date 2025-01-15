class Person:
    def __init__(self, name=[], surname='pen'):
        self.name = name
        self.surname = surname

    def add(self, name):
        self.name.append(self.name)

p1 = Person()
p1.add('Alex')
p1.add('Den')
print(p1.name, p1.surname)