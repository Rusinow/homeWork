# Инициализация
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15]
primes, not_primes = [], []
is_prime = True

# Основной блок скрипта

for i in numbers:
    for j in range(1, i):
        if i % j == 0 and j != 1:
            is_prime = False
            break
        is_prime = True
    if i == 1:              #исключение, число не является ни простым, ни составным
        continue            #по этому для него особое условие
    elif is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes: ', primes)
print('Not primes: ', not_primes)
