tupla = ('abundancia', 'abundante', 'acessivel', 'acessivel', 'aclamacao', 'aclamado', 'aclamacao', 'elogio', 'elogios', 'acomodatorio', 'acolhedor')
for t in tupla:
    print(f'{t:15}', 'Vogais: ', end=' ')
    for i in range(len(t)):
        if t[i] in 'aeiou':
            print(t[i], end=' ')
    print()
input()
