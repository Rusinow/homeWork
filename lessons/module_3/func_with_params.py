def func_with_params(a, b=2, c=None):
    if c is None:
        c = [a]
    print(c)


func_with_params(3)
func_with_params(5)
func_with_params(5)
func_with_params(5)