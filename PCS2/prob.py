import math
AT = 0
GC = 0
with open('rosalind_prob_new.txt', 'r') as f:
    for line in f:
        if line[0] != 'A' and line[0] != 'T' and line[0] != 'G' and line[
                0] != 'C':
            numbers = line.split()
            GC_contents = [float(x) for x in numbers]
        for i in line:
            if i == 'A' or i == 'T':
                AT += 1
            elif i == 'G' or i == 'C':
                GC += 1

probabilities = []
for j in range(len(GC_contents)):
    prob = math.log10((((1 - GC_contents[j]) / 2)**AT) * (GC_contents[j] / 2)
                      **GC)
    probabilities.append('%0.3f' % prob)
print(*probabilities, sep=' ')



    