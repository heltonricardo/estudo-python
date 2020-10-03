pessoas = []
temp = {}
while True:
    print()
    temp['nome'] = input('Nome...: ')
    temp['sexo'] = input('Sexo...: ')
    temp['idade'] = int(input('Idade..: '))
    pessoas.append(temp.copy())
    print()
    if input('Continuar? [S]im ou [N]ão: ') in 'Nn': break
print('Quantidade de cadastros..:', len(pessoas))
m = 0
for i in pessoas: m += i['idade']
m /= len(pessoas)
print('Média das idades.........:', m)
print('Mulheres:', end=' ')
for i in pessoas:
    if i['sexo'] == 'F': print(i['nome'], end='; ')
print()
print('Pessoas acima da média:', end=' ')
for i in pessoas:
    if i['idade'] > m: print(i['nome'], end='; ')
print()
input()
