a = int(input('Valor para A: '))
b = int(input('Valor para B: '))
print()
print('{} mais {} é ................... {}'.format(a, b, a + b))
print('{} subtraído de {} é ........... {}'.format(a, b, a - b))
print('{} multiplicado por {} é ....... {}'.format(a, b, a * b))
print('{} dividido (real) por {} é .... {:.3f}'.format(a, b, a / b))
print('{} elevado a {} é .............. {}'.format(a, b, a ** b))
print('{} dividido (inteiro) por {} é . {}'.format(a, b, a // b))
print('{} dividido por {} tem resto ... {}\n'.format(a, b, a % b))
print('Para não quebrar a linha', end=' ')
print('use print(), end=\' \'')
input()