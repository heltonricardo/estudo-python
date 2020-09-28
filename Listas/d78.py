val = list()
for i in range(5):
    val.append(int(input('Entre um inteiro: ')))
print('\nMaior valor:', max(val))
print('Posições:', end=' ')
for i in range(5):
    if max(val) == val[i]: print(i, end=' ')
print('\n\nMenor valor:', min(val))
print('Posições:', end=' ')
for i in range(5):
    if min(val) == val[i]: print(i, end=' ')
print()
input()
