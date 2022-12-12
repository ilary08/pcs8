import itertools
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
number = 3
repetion = itertools.product(letters, repeat=number)
for x,y in enumerate(list(repetion)):
    permutation = ''
    for item in y:
        permutation += str(item)
    with open('rosalind_lexf.txt', 'a') as text_file:
        print(permutation.strip()) 