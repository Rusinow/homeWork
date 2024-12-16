# int() --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
salary = [2300, 1800.8012354, 5000, 1234.58, 7500.12]
print(round(sum(salary)/len(salary), 2), 'средняя зарпалта в компании')
print(round(max(salary), 2),'- максимальная зарплата в компании')
print(round(min(salary), 2), '- минимальная зарплата в компании')

names = ['Denis', 'Anton', 'Egor', 'Katya', 'Evgen']

zipped = dict(zip(names, salary))
print(zipped['Denis'], 'зарплата дениса')