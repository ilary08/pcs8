from Bio import SeqIO
sequences= [] 
with open('rosalind_sseq.txt','r') as file:
   for record in SeqIO.parse(file,'fasta'):
       sequences.append(str(record.seq))
file.close()
x = sequences[0] #this is my position in the indices of s
y= sequences[1] # this my position in the indices t
p = 0
position = []
for i in range(len(y)):
    for j in range(p,len(x)):# i look through s and t
        p += 1
        if len(position) < len(y):
            if y[i] == x[j]: #we can have also multiple locations equal between them
                position.append(p) 
                break
print(*position, sep=' ')                 