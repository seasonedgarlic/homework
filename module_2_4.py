def is_prime(n):
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(n**0.5)+1, 2):
    if n % i == 0:
      return False
  return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
  if is_prime(i):
    primes.append(i)
  elif i == 1:
    i += 1
  else:
    not_primes.append(i)
print('Primes: ', primes)
print('Not Primes: ', not_primes)