pessoas = list()
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    c = str(input('Continuar? [S] para Sim: '))
    print()
    if not c in 'Ss': break
print('Quantidade de cadastros:', len(pessoas))
pesao = max(pessoas, key=lambda x: x[1])[1]
print('Maior peso: ' + str(pesao) + ' de: ', end='')
for i in pessoas:
    if i[1] == pesao: print(i[0], end='; ')
pesinho = min(pessoas, key=lambda x: x[1])[1]
print('\nMenor peso: ' + str(pesinho) + ' de: ', end='')
for i in pessoas:
    if i[1] == pesinho: print(i[0], end='; ')
print()
input()
