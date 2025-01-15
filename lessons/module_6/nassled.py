class Human:
    head = True

    def say_hello(self):
        print('Hello')

class Student(Human):
    head = False

    def about(self):
        print("I'm student")

class  Teacher(Human):
    pass




# human = Human()
student = Student()
teacher = Teacher()
student.say_hello()
teacher.say_hello()
# print(human.head)
print(student.head)