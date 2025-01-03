from encodings.punycode import insertion_sort

from Package1.alg import *

data_1 = list(map(int, input('Enter numbers separated by spaces: ').split()))
data_2 = list(map(int, input('Enter numbers separated by spaces: ').split()))
data_3 = list(map(int, input('Enter numbers separated by spaces: ').split()))

buble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print('buble_sort: ', data_1)
print('selection_sort: ', data_2)
print('insertion_sort: ', data_3)