n=int(input("digite o numero que deseja calcular o fatorial"))
fatorial=1
for i in range(1, n+1):
    fatorial *= i #fatorial=fatorial*i

print ("o fatorial de ,n é:" ,fatorial)
