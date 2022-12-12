def Fibonacci_Loop( months, offspring):
    parent, progeny = 1, 1
    for x in range(months - 1):
        progeny,parent = parent, parent + (progeny*offspring) #the population for each month is determined by the months before it, so using the Fibonacci sequence we sum the new generation with the generation before it in order to get the total number of rabbits
    return progeny
print(Fibonacci_Loop(35,5))    