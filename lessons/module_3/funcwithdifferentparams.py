# def test_func(*params ):
#     print('тип', type(params))
#     print('Аргумент', params)
#
#
# test_func(1, 2, 3, 4)
#
# def summator(txt, *values, type='sum'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
#
# print(summator('Summ numbers: ', 2, 3, 4, type='summator'))
#
#
# def info(value, *types, names_author = 'Sanek', **values):
#     print('тип', type(values))
#     print('Аргумент', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
#
#
# info('пример использования парамтров всех типов', 2, 3, 4, names_author='Alex', name = 'Aleksandr', course='Python')

def my_summ(n, *args, txt='summ numbers'):
    s = 0
    for i in range(len(args)):
        s += args[i] **n
    print(txt + ':', s)

my_summ(2, 1, 2, 3, 4, 5, txt = 'СУММА КВАДРАТОВ')
