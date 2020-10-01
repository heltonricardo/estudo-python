N1 = float(input('Entre a nota N1: '))
N2 = float(input('Entre a nota N2: '))
N3 = float(input('Entre a nota N3: '))
N4 = float(input('Entre a nota N4: '))
MD1 = (N1 + N2 + N3 + N4) / 4
if(MD1 >= 7.0):
    print('Aprovado com média {:05.2f}'.format(MD1))
else:
    NE = float(input('Entre nota de exame: '))
    MD2 = (NE + MD1) / 2
    if(MD2 >= 5.0):
        print('Aprovado em exame com média {:05.2f}'.format(MD2))
    else:
        print('Reprovado em média {:05.2f}'.format(MD2))
input()
