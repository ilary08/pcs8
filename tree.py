with open('rosalind_tree.txt', "r") as file:
    n = int(file.readline())
    adjacency_list = [line.strip().split(" ") for line in file]


subtrees = [] 
nodes = set() # I count the nodes as a set of lines connecting pairs of nodes
for i, j in adjacency_list: #I count how many paths are needed  
    if i in nodes or j in nodes:
        for st in subtrees:
            if i in st or j in st:
                subtrees[subtrees.index(st)].append(i)
                subtrees[subtrees.index(st)].append(j)
                nodes.add(i), nodes.add(j)
    else:
        subtrees.append([i,j])
        nodes.add(i), nodes.add(j) 

l = len(subtrees)
for i in range(l):
    for j in range(l):
        if i==j:
           break
        if len(set(subtrees[i] + subtrees[j])) < len(subtrees[i]) + len(subtrees[j]):
            subtrees[i] = list(set(subtrees[i] + subtrees[j]))
            subtrees[j] = []
subtrees = [i for i in subtrees if i]


result = (n -len(nodes)) + len(subtrees) - 1 #one set count as the base
print(result)
