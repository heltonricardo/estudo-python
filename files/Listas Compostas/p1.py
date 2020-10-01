pessoas = []
dados = []
print('ENTRE DADOS DE TRÊS PESSOAS')
for i in range(3):
    dados.append(str(input(f'\nNome {i + 1}...: ')))
    dados.append(str(input(f'Idade {i + 1}..: ')))
    pessoas.append(dados[:])
    print('Dados.....:', dados)
    print('Pessoas ..:', pessoas)
    dados.clear()
print('\nUsar dados.clear() depois de cada leitura para limpar lista dados')
print('Ao usar o append de uma lista em outra: [:]')
print('pessoas.append(dados[:]) para fazer cópia e não vínculo')
input()
