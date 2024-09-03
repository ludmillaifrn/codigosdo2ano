vetor = [87, 58, 25, 75, 66, 54, 46, 22, 93, 73, 1, 62, 4, 19, 86]
min = vetor[1]
max = vetor[1]

for i in range(1,len(vetor)):
    comp1 = vetor[i]
    comp2 = vetor[i-1]
    if comp1 > comp2:
        if max < comp1:
            max = comp1
        ver1 = comp2
        if ver1 < min:
            min = ver1
    elif comp1 < comp2:
        if min > comp1:
            min = comp1
        ver2 = comp2
        if ver2 > max:
            max = ver2

print(min, max)