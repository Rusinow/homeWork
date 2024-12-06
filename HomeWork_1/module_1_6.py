#работа со словарями

my_dict = {'Aleksandr': 1989, 'Olga': 1991, 'Nikolay': 1993} #создаем словарь
print('Dict:', my_dict)                                      #вывод словаря
print('Existing value:', my_dict.get('Nikolay'))             #вывод значения по ключу
print('not existing value:', my_dict.get('Marina'))          #вывод не существующего значения по ключу без ошибки
my_dict.update({'Alex': 1995,
                'Dima': 2001})                               #добавление двух новых пар в словарь
print('Deleted value:', my_dict.pop('Aleksandr'))            #удаление одной пары и вывод ее на экран
print('Modified dictionary:', my_dict)                       #вывод изменного словаря
print()                                                      #пустая строка для вывода задач

#работа с множествами

my_set = {1, 1, 1, 'Apple', 'Apple', 3.14}  #Создаем множество
print('Set:', my_set)                       #выводим множество
my_set.update([11, 'Orange', (5, 6 ,1.6)])  #добавляем произвольные обьекты в множество
my_set.discard(1)                           #удаляем элемент из множества
print('Modified set:', my_set)              #выводим измененное множество