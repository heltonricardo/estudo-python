from math import hypot
co = float(input('Cateto oposto....: '))
ca = float(input('Cateto adjacente.: '))
hip = hypot(co, ca)
print('\nHipotenusa: {}.'.format(hip))
input()
