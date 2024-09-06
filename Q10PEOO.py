# Função para verificar o sinal do número
def verificar_sinal(numero):
    if numero > 0:
        return "O número é positivo."
    elif numero < 0:
        return "O número é negativo."
    else:
        return "O número é zero."

# Recebe o número do usuário
numero = float(input("Digite um número: "))

# Verifica e exibe o resultado
resultado = verificar_sinal(numero)
print(resultado)