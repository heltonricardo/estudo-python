A = int(input('Entre valor para A: '))
B = int(input('Entre valor para B: '))
C = int(input('Entre valor para C: '))
if(A > B): A, B = B, A
if(A > C): A, C = C, A
if(B > C): B, C = C, B
print('Ordem crescente: {}, {} e {}'.format(A, B, C))
input()
