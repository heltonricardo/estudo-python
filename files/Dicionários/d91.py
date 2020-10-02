from random import randint
from time import sleep
temp = {}
banco = []
for i in range(4):
    temp['nome'] = 'jogador{}'.format(i+1)
    temp['valor'] = randint(1, 6)
    banco.append(temp.copy())
print('SORTEIO')
for j in banco:
    print(f'O {j["nome"]} tirou {j["valor"]}')
    sleep(1)
banco.sort(key=lambda k: k['valor'], reverse=True)
print()
print('RANKING')
for i, j in enumerate(banco):
    print(f'{i+1}º lugar: {j["nome"]} com {j["valor"]}')
    sleep(1)
