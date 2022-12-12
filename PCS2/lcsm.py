from Bio import SeqIO                      
sequences = []                             
with open('rosalind_lcsm.txt') as file:
 for record in SeqIO.parse(file, 'fasta'):
    sequence = []                          
    seq = ''                               
    for nt in record.seq:                  
        seq += nt                          
    sequences.append(seq)                  
file.close()
sorted_seq = sorted(sequences, key=len)     #I compare all the possible motifsin the shortest sequence, so first I sorted the list tp pick the shortest one
short_seq = sorted_seq[0]                   
comp_seq = sorted_seq[1:]                   
motif = ''                               
for i in range(len(short_seq)):          #The longest of the motifs that are present in all of the sequences is then saved and printed
    for j in range(i, len(short_seq)):   
        m = short_seq[i:j + 1]           
        found = False                   
        for sequ in comp_seq:            
            if m in sequ:                
                found = True            
            else:                        
                found = False           
                break                   
        if found and len(m) > len(motif):
            motif = m                    
print(motif)