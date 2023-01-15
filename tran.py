from Bio import SeqIO
sequences = []
with open('rosalind_tran.txt', 'r') as file:
    for record in SeqIO.parse(file,'fasta'):
        sequences.append(str(record.seq))        
file.close()                               
s1 = sequences[0]  #the s1 and s2 have the same lenght and we define them as the ratio of the number of transitions to the number of transversions                      
s2 = sequences[1]                   
transition = 0
transversion = 0
purines = ['A','G'] #nucleotides at the corresponding positions between the two DNA sequences are compared with each other.
pirimidines = ['C','T']
for nt1, nt2 in zip(s1, s2):                 
    if nt1 != nt2:                           
        if nt1 in purines and nt2 in purines:          
            transition += 1                  
        elif nt1 in pirimidines and nt2 in pirimidines:        
            transition += 1                  
        else:                                
            transversion += 1                
print('%0.11f' % (transition / transversion))