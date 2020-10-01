def potencia(b, e):
    r = 1
    for i in range(e):
        r *= b
    return r

b = int(float(input('Entre a base inteira.....: ')))
e = int(float(input('Entre o expoente inteiro.: ')))
print()
print('{} ^ {} = {}'.format(b, e, potencia(b, e)))
input()
