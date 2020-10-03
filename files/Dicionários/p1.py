print('pessoas = {\'nome\': \'Helton\', \'sexo\': \'M\', \'idade\': 24}')
pessoas = {'nome': 'Helton', 'sexo': 'M', 'idade': 24}
print()
print('print(\'pessoas\'):', pessoas)
print('print(\'pessoas.values()\'):', pessoas.values())
print('print(\'pessoas.keys()\'):', pessoas.keys())
print('print(\'pessoas.items()\'):', pessoas.items())
print()
print('print(f\'O {pessoas["nome"]} tem {pessoas["idade"]} anos.\'):')
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()
print('pessoas[\'peso\'] = 83')
pessoas['peso'] = 83
print('print(\'pessoas\'):', pessoas)
print('del pessoas[\'peso\']')
del pessoas['peso']
print('print(\'pessoas\'):', pessoas)

input()
