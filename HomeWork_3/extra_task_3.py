def calculate_structure_sum(args):
    """calculates the sums of all numbers and the lengths of all strings"""
    structure_summ = 0
    if isinstance(args, int):
        return args
    elif isinstance(args, str):
        return len(args)
    elif isinstance(args, dict):
        for k, v in args.items():
            structure_summ += calculate_structure_sum(k)
            structure_summ += calculate_structure_sum(v)
    elif isinstance(args, (tuple, set, list)):
        for i in args:
            structure_summ += calculate_structure_sum(i)
    return structure_summ

# Входные данные (применение функции):
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)