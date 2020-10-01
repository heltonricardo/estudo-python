resp = 's'

while not (resp.upper() == 'N'):
    n = int(input('Entre valor para tabuada: '))
    i = 1
    while (i <= 9):
        r = n * i
        print('{:3} x {} = {:3}'.format(n, i, r))
        i = i + 1
    resp = input('Entre [N] para sair: ')
    print()
input()
