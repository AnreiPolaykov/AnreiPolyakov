def apply_all_func(int_list: list, *functions):
    resulte: dict = {}
    for func in functions:
        res = func(int_list)
        resulte[func.__name__] = res
    return resulte
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
