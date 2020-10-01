A = int(input('Entre inteiro para A: '))
B = int(input('Entre inteiro para B: '))
C = int(input('Entre inteiro para C: '))
D = int(input('Entre inteiro para D: '))
E = int(input('Entre inteiro para E: '))

maior = A if(A > B) else B
maior = C if(C > maior) else maior
maior = D if(D > maior) else maior
maior = E if(E > maior) else maior

print('\nO maior valor entrado foi', maior)
input()
