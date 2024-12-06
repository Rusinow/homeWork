immutable_var = 1, 2, 'a', 'b'
print('immutuble tuple:', immutable_var)

#immutable_var[0] = 0
'''попытка изменения кортежа 
TypeError: 'tuple' object does not support item assignment
кортеж(tuple) - неизменяемый объект'''

mutable_list = [1, 2, 'a', 'b', 'c']
mutable_list [4] = 'Modified'
print('Mutable list:', mutable_list)