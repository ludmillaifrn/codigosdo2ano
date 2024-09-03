def C_para_F(C):
    F = (C*9/5) + 32
    return F

def F_para_C(F):
    C = (F-32)*5/9
    return C


def menu():
    while True:
        op = int(input('1. Celsius para Farenheit: \n' +
                       '2. Farenheit para Celsius: '))

        if op==1:
            C=int( input('Graus Celsius: ') )
            print('Convertido: ', C_para_F(C),' graus Farenheit\n')
        elif op==2:
            F=int( input('Graus Farenheit: ') )
            print('Convertido: ', F_para_C(F),' graus Celsius\n')
        else:
            print('Opção inválida')
menu()