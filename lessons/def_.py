import random
def lottery(*args, **kwargs):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2

win1, win2 = lottery(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(win1, win2)

def test(a=2, b=True):
    print(a,b)
