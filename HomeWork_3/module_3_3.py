def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,  2, 3])

values_list = [2, 'two', False]
values_dict = {'a': 3, 'b': 'three', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [4, 'four']

print_params(*values_list_2, 42)