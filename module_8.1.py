def add_everything_up(a, b):
    try:
        c = a + b
        return c
    except TypeError:
        return f'{a}{b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

'''так же подобных выводов можно добиться с помощью пользовательского ввода
def add_everything_up(a = input(), b = input()):
    c = a + b
    return c
print(add_everything_up())'''