n = int(input('Valor para tabuada: '))

for i in range(0, 10):
    # vai de 0 até 9 de 1 em 1
    # mesmo efeito com range(10)
    r = n * i
    print('{:3} x {} = {:3}'.format(n, i, r))
input()
