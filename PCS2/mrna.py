codons = {                                                     
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G' 
}                                                              

def codon_frequence():                    #first I focused on the rna table dictionary                     
    frequence = {}                                             
    for k,x in codons.items():                                
        if x not in frequence:                                 
            frequence[x] = 0                                   
        frequence[x] += 1                                      
    return (frequence)                                         


def possible_sequences(sequence):       #here we focused on the possible frequencies
    f = codon_frequence()               #every possible sequence encodes the given protein, there are three possible stop codons                       
    n = f['Stop']                                              
    for aa in sequence:                                        
        n *= f[aa]                    # the frequency of the possible sequences becomes three times the number of codons that each amino acid in the protein could be encoded by                          
    return (n % 1000000)                                       


with open('rosalind_mrna.txt', 'r') as file:                         
    proton_sequence = file.read().strip()                                
print(possible_sequences(proton_sequence))