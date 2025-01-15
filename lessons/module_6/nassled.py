class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello():
        print('Hello')

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    pass
    # def about(self):
    #     print("I'm student")

class  Teacher(Human):
    pass

human = Human()
human.about()
student = Student()
