from pprint import pprint
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3],[4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
final_grade = {}
n = 0
for student in students:
    final_grade[student] = sum(grades[n]) / len(grades[n])
    n += 1
pprint(final_grade)