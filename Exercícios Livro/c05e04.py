def modulo(n):
    m = -n if (n < 0) else n
    print('O módulo de {} é {}'.format(n, m))

n = int(float(input('Entre um inteiro negativo ou positivo: ')))
modulo(n)
input()
