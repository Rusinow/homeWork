a = 5
b = 10

print(a, b)

def printer():
    global a, b
    a = 'Str'
    b = 'Str2'
    c = 15
    d = 20
    print(c, d, 'local')
    print(a, b, 'global')

print(a, b)
printer()
print(a, b)