import random as rng

n = rng.randint(3, 20)
pairs = list(range(1, 21))
result = []
for i in range(len(pairs)):
  for j in range(i + 1, len(pairs)):
    if n % (pairs[i] + pairs[j]) == 0:
      result.append((pairs[i], pairs[j]))
    
print(f'{n} - {result}') 
