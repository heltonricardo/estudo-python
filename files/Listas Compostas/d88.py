from random import sample
print('= PROGRAMA MEGASENA =')
n = int(input('\nQuantidade de jogos: '))

jogos = []
for i in range(n):
    jogos.append([sorted(sample(range(1, 61), 6))])
    print(f'Jogo {i + 1:2}:', jogos[i])
input()
