def print_params(**kwargs): # *arcs, **kvargs
    for key, value in kwargs.items():
        print(key, value)

dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)