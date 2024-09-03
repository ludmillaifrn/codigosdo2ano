numero = int(input("Digite um número positivo e inteiro: "))

def exibir_numeros_pares(numero):
    if numero <= 0:
        print("digite um numero positivo e inteiro")
    print("Números pares menores que", numero, ":")
    for i in range(numero):
        if i % 2 == 0:
            print(i)

exibir_numeros_pares(numero)