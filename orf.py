DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def complementary_dna(dna_string):
    base_replaced = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} #to find the complementary DNA strand we associate to each pirimidine its purine
    for base in reversed(dna_string):
        return ''.join([base_replaced[base]])     
    
    def translate(fragment):
        peptide =[]
        methionine = fragment.find('ATG') #translation of DNA into aminoacid starting with methionine
        codons = [fragment[methionine:methionine+3] for methionine in range(methionine, len(fragment), 3)]
        for codon in codons:
            peptide += DNA_CODON_TABLE.get(codon)
        return ''.join(map(str, peptide))
    import re
 
    pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAA|TAG|TGA))') #before translating we check codons that corrispond to methionine and stop codons (TAA, TAG or TGA)
 
    fragments = []
    for string in re.findall(pattern, dna_string):
        fragments.append(string)
 
    for string in re.findall(pattern, complementary_dna(dna_string)):
        fragments.append(string)
        
    with open("rosalind_orf.txt", 'r') as file:
        for line in file:
            if line.startswith(">"):
                nextline = str()
            else:
                nextline += (line.strip("\n"))
            dna_string = nextline
 
    for string in set(fragments):
        print(translate(string))

        
