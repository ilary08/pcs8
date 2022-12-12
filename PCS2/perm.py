import math                                         
import itertools                                    
number_of_permutations = 6                                     
print(math.factorial(number_of_permutations))                            
perm = itertools.permutations(list(range(1, number_of_permutations + 1)))
for i, j in enumerate(list(perm)):                  
    permutation = ''                                
    for item in j:                                  
        permutation += str(item) + ' '              
    print(permutation)                              
