def print_params(a = 1, b = 'строка', c = True):
        print(a, b, c)
        print(f'a : {a}', f'b : {b}', f'c : {c}')
print_params(b=25)
print_params(c = [1,2,3])

values_list = [ 33, 'Hai', False]
print_params(*values_list)
values_dict = {'a':values_list[0], 'b':values_list[1], 'c':values_list[2]}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)















