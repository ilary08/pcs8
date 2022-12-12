def Longest(n1, n2, func):
    my_list = []
    new_list = []
    for i in range(n1):
        my_list.append(1)
        new_list.append([n2[i]])
        for x in range(i):
            if func(n2[x], n2[i]):
                my_list[i] = max(my_list[i], my_list[x] + 1)
                if len(new_list[i]) <= len(new_list[x]):
                    new_list[i] = new_list[x] + [n2[i]]
    return max(my_list, new_list[my_list.index(max(my_list))])
with open('rosalind_lgis.txt', 'r') as file:
   n1 = int(file.readline().strip())
   n2 = list(int(i) for i in file.readline().strip().split(" "))
print(*Longest(n1,n2, lambda a, b: a<b))
print(*Longest(n1,n2, lambda a, b: a>b))                        