def Mortal_Fibonacci(n, m):
    living_generation = [1,1] #here parents and progeny are both alive
    for x in range (2, n):
        first_reproduction= living_generation[x-1] + living_generation[x-2]
        #rabbits die 
        if x == m: # after months m the parents die so we don't count them  
            first_reproduction = first_reproduction-1
        elif x>m:
            first_reproduction = first_reproduction - living_generation[x-m-1]#we keep track of the reamaing population after time m

        living_generation.append(first_reproduction)
    return living_generation[-1]
print(Mortal_Fibonacci(84,16))
