from Bio import SeqIO
from math import factorial

sequence = ''                              
handle = open('rosalind_pmch.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequence = str(record.seq)             
handle.close()

AU = 0
GC = 0
for matching in sequence:
    if matching == 'A': #i used the simple counter method to check all the matchings
        AU += 1
    elif matching == 'G': #the base pairs are considered as edges and as one possibility of base pairing interactions 
        GC += 1
final_result = factorial(AU) * factorial(GC) #I had to multiply to get the total amout of matching 
print(final_result)        
