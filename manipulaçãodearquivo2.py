import os

def criar_questionario():
    n = int(input("Número de entrevistados: "))
    dados = [{"nome": input("Nome: "), "idade": int(input("Idade: ")), "resposta": input("Resposta: ")} for _ in range(n)]
    with open("dados.os", "w") as arquivo:
        os.dump(dados, arquivo)
    print("Dados salvos!")

def ler_dados():
    try:
        with open("dados.os", "r") as arquivo:
            for d in os.load(arquivo):
                print(f"Nome: {d['nome']}, Idade: {d['idade']}, Resposta: {d['resposta']}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

while (op := input("\n1. Criar\n2. Ler\n3. Sair\nEscolha: ")) != "3":
    criar_questionario() if op == "1" else ler_dados() if op == "2" else print("Opção inválida.")
