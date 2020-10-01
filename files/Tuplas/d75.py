n = []
for i in range(4):
    n.append(int(input(f'Insira o {i + 1}º valor: ')))
tupla = (n[0], n[1], n[2], n[3])
print(tupla)
print('Quantidade de 9 na tupla:', tupla.count(9))
if 3 in tupla:
    print('Primeiro 3 digitado na posição:', tupla.index(3))
print('Números pares:', end=' ')
for i in range(4):
    if tupla[i] % 2 == 0:
        print(tupla[i], end=', ')
print()
input()
