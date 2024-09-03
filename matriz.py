matriz = [['2','4','8'],
          ['3','9','27'],
          ['4','16','64']]
transposta = [list(coluna) for coluna in zip(*matriz)]
for linha in transposta :
    print(linha)
