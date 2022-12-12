# open the file with the data
data = open('rosalind_hamm.txt', "r")

    #read it but then split by lines, and store as a list in dataset
dataset = data.read().splitlines()

    #the first item in the dataset is the first line
firststring = dataset[0]

    #the second item is the second line
secondstring = dataset[1]

count = 0
for i in range(len(firststring)):
    if firststring[i] != secondstring[i]:
        count +=1
print (count)