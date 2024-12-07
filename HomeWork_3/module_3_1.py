calls = 0

def count_calls():
    '''подсчитывает вызов остальных функций'''
    global calls
    calls += 1

def string_info(string):
    ''' принимает аргумент - строку и возвращает кортеж из:
     длины этой строки, строку в верхнем регистре, строку в нижнем регистре'''
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_

def is_contains(string:str, list_to_search:list):
    '''принимает два аргумента: строку и список,
     и возвращает True, если строка находится в этом списке, False - если отсутствует'''
    count_calls()
    overlap = True
    list_UP = []
    for i in list_to_search:
        list_UP.append(i.upper())
    if string.upper() not in list_UP:
        overlap = False
    return overlap

# Пример выполняемого кода:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)