set_ = {1, 2, 3, 4, 5, 6, 7, 4 , 3, True, 'string', (1, 2, 3,)}
list_ = [1, 1, 1, 1, 1, 2, 3, 2, 2, 2]
list_ = set(list_)
print(list_)
print(list_.remove(1))      #удаление элемента из множества
print(list_.discard(1))     #удаление элемента из множества без ошибки если элемента нет.
print(list_.pop())
print(list_)
print(list_.add(5))
print(list_)