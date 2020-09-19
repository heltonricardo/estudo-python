frase = input('Entre uma frase: ').lower().replace(' ', '')

if frase == frase[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

input()
