from math import factorial 
n = 100
k = 9
permutations = (factorial(n)/factorial(n-k)) % 1000000
print(permutations)