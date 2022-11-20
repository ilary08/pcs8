import math 

k = 5 #num of generation  
n = 8 #number of success  
p = 2 ** k #population at given generation k^2
prob = 0
for x in range(n,p+1):
    probability = (math.factorial(p) / (math.factorial(x) * math.factorial(p-x))) * (0.25**x) * (0.75**(p-x)) #fraction got from the calculations from the punnet square
    prob += probability
print(round(prob,3))
    
