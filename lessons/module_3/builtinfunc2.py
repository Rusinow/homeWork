a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
c[0] = 2
print(id(a))
print(id(d))
print(a is d)
print(id(c))
print(c is d)

def helper():
    '''это функция - помошнил'''
    pass

print(helper.__doc__)