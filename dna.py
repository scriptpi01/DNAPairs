dna_1, dna_2  = str(input()), str(input())
dna1, dna2 = list(dna_1), list(dna_2)
collect1 = []
collect2 = []
all = []
for i in range(len(dna1)):
    for j in range(i+1):
        collect1.append(dna1[j:len(dna1)-(i-j)])
for i in range(len(dna2)):
    for j in range(i+1):
        collect2.append(dna2[j:len(dna2)-(i-j)])

for i in range(len(collect1)):
    for j in range(len(collect2)):
        if collect1[i] == collect2[j]:
            all.append(collect1[i])
            break
        else:
            pass
print(''.join(all[0]))

#print(*all)






"""
[['a', 'b', 'c', 'd'], 
['a', 'b', 'c'], ['b', 'c', 'd'], 
['a', 'b'], ['b', 'c'], ['c', 'd'], 
['a'], ['b'], ['c'], ['d']]

collect1.append(dna1[0:len(dna1)-0])

collect1.append(dna1[0:len(dna1)-1])
collect1.append(dna1[1:len(dna1)-0])

collect1.append(dna1[0:len(dna1)-2])
collect1.append(dna1[1:len(dna1)-1])
collect1.append(dna1[2:len(dna1)-0])

collect1.append(dna1[0:len(dna1)-3])
collect1.append(dna1[1:len(dna1)-2])
collect1.append(dna1[2:len(dna1)-1])
collect1.append(dna1[3:len(dna1)-0])

AAAACTGCTACCGGT
CTGAATCTACTGCTATTGCAA
"""
