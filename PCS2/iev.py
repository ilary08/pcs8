with open('rosalind_iev.txt', 'r') as values:
    sep_values = values.read().split()
    a = int(sep_values[0])
    b = int(sep_values[1])
    c = int(sep_values[2])
    d = int(sep_values[3])
    e = int(sep_values[4])
    f = int(sep_values[5])

    final_result = (a * 2 * 1) + (b * 2 * 1) + (c * 2 * 1) + (d * 2 * 0.75) + (e * 2 * 0.5) + (f * 2 * 0) #I moltiplied by two because each parents as two children and then I multiplied for the probability of having a dominant genotype, which I've got from the punnet square 
    print(final_result)