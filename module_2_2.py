#The program takes three random numbers and outputs the number of identical ones
first = input('enter the first number: ')
second = input('enter the second number: ')
third = input('enter the third number: ')
if first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
else:
    print(0)