from random import sample

tupla = tuple(sample(range(100), 5))
for i in tupla:
    print(i, end=' ')
print('\nMenor valor:', min(tupla))
print('Maior valor:', max(tupla))
input()
