with open ('./rosalind_dna.txt', )as dna_string:

    counter_A = 0
    counter_G = 0
    counter_C = 0
    counter_T = 0
    for nucleotide in dna_string :    
        if nucleotide == 'A':
            counter_A += 1
        if nucleotide == 'G':
            counter_G += 1
        if nucleotide == 'C':
            counter_C += 1
        if nucleotide == 'T':
            counter_T += 1
    print(counter_A, counter_C)
    print(counter_G,counter_T)

