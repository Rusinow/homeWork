food = ['apple', 'coconut', 'banana'] #создание списка
food.append(True)                        #добавление в конец списка нового значения
print(food)                               #вывод списка
food.extend(['string', 2])                #добавление в конец списка
print(food)                             #вывод нового списка
food.remove('apple')                  #удаление значения по названию
print(food)                             # вывод обновленного значения
print('coconut' in food)                 #проверка наличия значения в списке
print('coconut' not in food)               #проверка отсутсвия знаяения в списке
print(food[0:2:2])                          #вывод значения с нулвого до второго с шагом два

tuple_ = 1, 2, 3, True, 'String'         #созание кортежа
list_ = [1, 2, 3, True, 'String']       #создание списка
tuple_2 = (1, 2, 3, 4)                   #второй способ создания кортежа
tuple_3 = tuple([1, 2, 3, 4])          #третий способ создания кортежа
print(tuple_2)                          #вывод кортежа 2
print(tuple_3)                           #вывод кортежа 3
print(tuple_.__sizeof__())                 #проверка занимаемой памяти кортежа
print(list_.__sizeof__())              #проверка занимаемой памяти списком
tuple_ = ([1, 2], 0) + (1, 2)             #сложение кортежей
print(tuple_)                           #вывод резльтата сложения кортежей
tuple_[0][0] = 2                        #замена переменной списка в кортеже
print(tuple_)                            #вывод кортежа с изменной переменной вложенного списка
tuple_ = (1, 2) * 3                      #умножение кортежей
print(tuple_)                            #вываод перемноженного кортежа
