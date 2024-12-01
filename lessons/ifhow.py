#name = input('What is your name?:')
#if name == 'Alex':
#    print('Hello administrator!')
#else: print('Hello', name)
number = int(input('Enter number: ')) #Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print('number not ready')