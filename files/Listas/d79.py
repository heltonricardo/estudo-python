val = []
while True:
    n = int(input('Entre um inteiro ou [0] para finalzar: '))
    if n == 0: break
    if not n in val: val.append(n)
print('\nLista crescente sem repetição:', sorted(val))
input()
