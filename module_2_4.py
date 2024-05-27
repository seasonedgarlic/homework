numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
x = 0
for i in range(2, 16):
    for j in range(2, i):
        if i % j == 0:
            x += 1
    if x == 0:
        primes.append(i)
    else:
        x = 0
        not_primes.append(i)
print("Primes: ", (primes))
print("Not primes: ", (not_primes))