def is_prime(func):
    def wrapper(*args, **kwargs):
        k = func(*args, **kwargs)
        if k > 1:
            for i in range(2, int(k/2) + 1):
                if k % i == 0:
                    print("Составное")
                    break
            else:
                print('Простое')
        else:
            print('Простое')
        return k
    return wrapper

@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res

ololo = sum_three(2,3,6)
print(ololo)