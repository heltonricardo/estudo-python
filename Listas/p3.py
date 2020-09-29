lista = []
print('lista = [] ou lista = list() para criar lista vazia')
lista.append('D')
lista.append('B')
lista.append('A')
lista.append('C')
lista.append('E')
print('\nLista =', lista,'\n')
print('for c, v in enumerate(lista): print(f\'IND[{c}] = {v})\')')
for c, v in enumerate(lista):
    print(f'IND[{c}] = {v}')
input()
