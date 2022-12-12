from Bio import SeqIO                           

record = SeqIO.read('rosalind_revp.txt', 'fasta')
forward_seq = str(record.seq)         #I compare the forward sequence with the complementary string and I pick out all the pieces >=4 or <=12
reverse_seq = str(record.seq.complement())
for i in range(len(forward_seq)):                   
    for j in range(i, len(forward_seq)):            
        m = forward_seq[i:j + 1]                    
        rev_m = reverse_seq[i:j + 1]                
        if len(m) >= 4 and len(m) <= 12:        
            if m == rev_m[::-1]:                
                print(i + 1, len(m)) #I print the position and the size of the palindrome