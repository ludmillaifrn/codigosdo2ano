import tkinter as tk
from tkinter import ttk

# Função para carregar os dados do arquivo
def carregar_dados_txt():
    try:
        with open("reservas.txt", "r") as f:
            return [line.strip().split('|') for line in f.readlines()]
    except FileNotFoundError:
        return []

# Função para salvar dados no arquivo
def salvar_dados_txt(dados):
    with open("reservas.txt", "a") as f:
        f.write("|".join(dados) + "\n")

# Função para verificar duplicidade de CPF
def cpf_duplicado(cpf):
    return any(dado[8] == cpf for dado in carregar_dados_txt())

# Função para consultar cadastro
def consultar_cadastro():
    def buscar():
        campo, valor = campo_busca.get(), valor_busca.get()
        if campo not in ["Nome", "CPF"]:
            resultado_label.config(text="Escolha Nome ou CPF para busca.", fg="red")
            return
        idx = 0 if campo == "Nome" else 8  # Nome na posição 0 e CPF na posição 8
        resultado = next((dado for dado in carregar_dados_txt() if dado[idx] == valor), None)
        if resultado:
            resultado_label.config(text="\n".join([f"{campo}: {v}" for campo, v in zip(campos, resultado)]), fg="green")
        else:
            resultado_label.config(text="Cadastro não encontrado!", fg="red")

    janela = tk.Tk()
    janela.title("Consultar Cadastro")

    tk.Label(janela, text="Buscar por:").grid(row=0, column=0)
    campo_busca = ttk.Combobox(janela, values=["Nome", "CPF"])
    campo_busca.grid(row=0, column=1)

    tk.Label(janela, text="Digite aqui:").grid(row=1, column=0)
    valor_busca = tk.Entry(janela)
    valor_busca.grid(row=1, column=1)

    tk.Button(janela, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2)

    resultado_label = tk.Label(janela)
    resultado_label.grid(row=3, column=0, columnspan=2)

    janela.protocol("WM_DELETE_WINDOW", lambda: confirmar_saida(janela))  # Intercepta o evento de fechamento
    janela.mainloop()

# Função para enviar dados do formulário
def enviar_dados(entradas):
    dados = [entradas[campo].get() for campo in campos]
    if any(not dado for dado in dados):
        mensagem_label.config(text="Preencha todos os campos!", fg="red")
    elif cpf_duplicado(dados[8]):
        mensagem_label.config(text="Estas informações já foram cadastradas!", fg="red")
    else:
        salvar_dados_txt(dados)
        mensagem_label.config(text="Cadastro realizado!", fg="green")
        [entrada.delete(0, tk.END) for entrada in entradas.values()]

# Função para abrir o formulário de reserva
def abrir_formulario():
    global janela, mensagem_label
    janela = tk.Tk()
    janela.title("Formulário de Reserva")
    
    entradas = {campo: tk.Entry(janela) for campo in campos}
    
    for i, campo in enumerate(campos):
        tk.Label(janela, text=f"{campo}:").grid(row=i, column=0)
        entradas[campo].grid(row=i, column=1)

    mensagem_label = tk.Label(janela)
    mensagem_label.grid(row=len(campos), column=0, columnspan=2)

    tk.Button(janela, text="Enviar", command=lambda: enviar_dados(entradas)).grid(row=len(campos)+1, column=0, columnspan=2)

    janela.protocol("WM_DELETE_WINDOW", lambda: confirmar_saida(janela))  # Intercepta o evento de fechamento
    janela.mainloop()

# Função para mostrar os tipos de quartos
def mostrar_tipos_quartos():
    tipos = [
        "Suíte: R$ 4.500, (hidromassagem, piscina, espaço kids, academia, spa, area de drinks, serviço de quarto 24hrs)",
        "Duplo: R$ 2.500 (cama king-size, piscina, espaço kids, spa, academia, drinks)",
        "Simples: R$ 1.000 (piscina, espaço kids, spa, academia)"]
    janela = tk.Tk()
    janela.title("Tipos de Quartos")
    for i, tipo in enumerate(tipos):
        ttk.Label(janela, text=tipo).grid(row=i, padx=10, pady=2)

    ttk.Button(janela, text="Continuar", command=lambda: [janela.destroy(), abrir_formulario()]).grid(row=len(tipos), pady=10)
    
    janela.protocol("WM_DELETE_WINDOW", lambda: confirmar_saida(janela))  # Intercepta o evento de fechamento
    janela.mainloop()

# Função para a tela inicial
def tela_inicial():
    root = tk.Tk()
    root.title("Hotel Copacabana Palace")
    ttk.Label(root, text="Olá, bem-vindo ao site do Hotel Copacabana Palace! :)").grid(row=0, padx=10, pady=5)
    ttk.Button(root, text="Entrar", command=lambda: [root.destroy(), mostrar_tipos_quartos()]).grid(row=1, pady=10)
    ttk.Button(root, text="Consultar Cadastro", command=lambda: [root.destroy(), consultar_cadastro()]).grid(row=2, pady=10)

    root.protocol("WM_DELETE_WINDOW", lambda: confirmar_saida(root))  # Intercepta o evento de fechamento
    root.mainloop()

# Função para confirmar a saída
def confirmar_saida(janela):
    confirmacao_janela = tk.Toplevel(janela)
    confirmacao_janela.title("Confirmar saída")

    ttk.Label(confirmacao_janela, text="Deseja sair mesmo?").grid(row=0, column=0, padx=10, pady=10)
    
    def sair():
        janela.destroy()
        confirmacao_janela.destroy()
    
    def cancelar():
        confirmacao_janela.destroy()

    ttk.Button(confirmacao_janela, text="Sim", command=sair).grid(row=1, column=0, padx=10, pady=5)
    ttk.Button(confirmacao_janela, text="Não", command=cancelar).grid(row=1, column=1, padx=10, pady=5)

# Definição dos campos de cadastro
campos = ["Nome", "Quantos quartos deseja?", "Email", "Check-in", "Check-out", "Telefone", "Tipo de quarto", "Quantidade de Pessoas", "CPF"]

# Chama a tela inicial
tela_inicial()
