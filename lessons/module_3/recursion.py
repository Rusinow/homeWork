def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n-1)


print(summa(5))

stack = []
stack.append(1)
print('Добавили элкмент', stack)
stack.append(2)
print('Добавили элкмент', stack)
stack.append(3)
print('Добавили элкмент', stack)
print(stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
print(stack)