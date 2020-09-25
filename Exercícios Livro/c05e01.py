def somatorio(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

valor = int(float(input('Entre um valor inteiro: ')))
print('A soma de 1 até {} é {}'.format(valor, somatorio(valor)))
input()
