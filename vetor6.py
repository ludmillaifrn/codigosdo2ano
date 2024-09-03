vet = [87, 58, 25, 75, 66, 54, 46, 22, 93, 73, 1, 62, 4, 19, 86]

for i in range(len(vet)):
    for j in range(0, len(vet)-1):
        if vet[j] > vet[j+1]:
            aux = vet[j]
            vet[j] = vet[j+1]
            vet[j+1] = aux

print(vet)
