A = int(input('Entre inteiro para A: '))
B = int(input('Entre inteiro para B: '))
C = int(input('Entre inteiro para C: '))
D = int(input('Entre inteiro para D: '))

if not(A % 2 == 0 and A % 3 == 0):
    print('{:4} não é divisível por 2 e 3.'.format(A))
if not(B % 2 == 0 and B % 3 == 0):
    print('{:4} não é divisível por 2 e 3.'.format(B))
if not(C % 2 == 0 and C % 3 == 0):
    print('{:4} não é divisível por 2 e 3.'.format(C))
if not(D % 2 == 0 and D % 3 == 0):
    print('{:4} não é divisível por 2 e 3.'.format(D))
input()
