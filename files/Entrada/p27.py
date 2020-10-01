from random import shuffle
n1 = input('Entre o nome 1: ')
n2 = input('Entre o nome 2: ')
n3 = input('Entre o nome 3: ')
n4 = input('Entre o nome 4: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print()
print('Ordem: {}'.format(lista))
input()
