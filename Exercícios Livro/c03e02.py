N1 = float(input('Nota N1: '))
N2 = float(input('Nota N2: '))
N3 = float(input('Nota N3: '))
N4 = float(input('Nota N4: '))
MD = (N1 + N2 + N3 + N4) / 4
if(MD >= 5.0):
    print('Aprovado', end=' ')
else:
    print('Reprovado', end=' ')
print('{:05.2f}'.format(MD))
input()
