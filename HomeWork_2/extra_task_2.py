
n = int(input('Введите число (от 3 до 20): '))

def search_for_couples():
    '''ищет все уникальные пары чисел для числа "n"'''
    list_n = []
    for i in range(n):
        if i == 0:
            continue
        list_n.append(i)
    all_couples = []
    for i in list_n:
        k = 1
        for i2 in list_n:
            if i2 <= i:
                k += 1
                continue
            all_couples.append([i, i2])
    return all_couples

def finding_multiples():
    '''ищет все делители из списка пар для числа "n"'''
    multiples = []
    k = 0
    for i in couples:
        if n % (couples[k][0] + couples[k][1]) == 0:
            multiples.append(i)
        k += 1
    return multiples

couples = search_for_couples()
result = finding_multiples()

print(*result)
