def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25) #вызов работает, так как a и c определены, а b переопределяется
print_params(c = [1,2,3])
list = [1, 2, 3]
print_params(list)
print_params(*list)

values_list = [99, 777, 666.6]
values_dict = {'a': 5, 'b': 6, 'c': 7}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) #вызов работает, так как элементы списка аргами последовательно передаются первым двум параметрам, а последний третий мы переопределяем отдельно