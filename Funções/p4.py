raiz = lambda base, exp: base ** (1 / exp)

print('=== RAÍZ :: USO DE LAMBDA, VER CÓDIGO ===')
print()
b = int(float(input('Entre valor para base.....: ')))
e = int(float(input('Entre valor para expoente.: ')))
print()
print('Raíz de {} com índice {} é igual a {}'.format(b, e, raiz(b, e)))
input()
