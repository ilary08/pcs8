max_gc = 0
with open('rosalind_gc_n.txt', 'r') as f:
    fasta = f.readlines()
    for i, line in enumerate(fasta):
            if line.startswith('>'):
                id = line[1:]
                
                seq = ''
            else:
                newseq = line.strip()
                seq = seq + newseq
               
                if i==len(fasta)-1 or fasta[i+1].startswith('>'):
                    gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
                    if gc > max_gc:
                        max_gc = gc
                        max_id = id

print(max_id, end='')
print(max_gc)

    