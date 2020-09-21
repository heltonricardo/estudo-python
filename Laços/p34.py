n = int(input('Valor para tabuada: '))

for i in range(1, 11):
    r = n * i
    print('{:3} x {:2} = {:3}'.format(n, i, r))
input()
