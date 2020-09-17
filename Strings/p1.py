frase = 'Helton Ricardo Santos da Costa'

print('frase:  ', frase)
print('índices: 012345678911234567892123456789')
print('range: [começo:fim]')
print('range: [começo:fim:incremento]')
print()
print('frase[0]:  ', frase[0])
print('frase[0:7]:', frase[0:6])
print('frase[0:9]:', frase[0:9])
print('frase[3:13:2]:', frase[3:13:2])
print('frase[:5]:', frase[:5])
print('frase[5:]:', frase[5:])
print('frase[9::3]:', frase[9::3])
print()
print('len(frase):', len(frase))
print('frase.count(\'o\'):', frase.count('o'))
print('frase.count(\'o\', 0, 15):', frase.count('o', 0, 15))
print('frase.find(\'a\'):', frase.find('a'))
print('frase.find(\'M\'):', frase.find('M'))
print('\'R\' in frase:', 'R' in frase)
print()
print('frase.replace(\' \', \'_\'):', frase.replace(' ','_'))
print('frase.upper():', frase.upper())
print('frase.lower():', frase.lower())
print('frase.capitalize():', frase.capitalize())
print('frase.title():', frase.title())
print()
frase = '   Helton Ricardo Santos da Costa   '
print('frase: {} (espaços antes e depois)'.format(frase))
print('frase.strip():', frase.strip())
print('frase.rstrip():', frase.rstrip())
print('frase.lstrip():', frase.lstrip())
print()
frase = 'Helton Ricardo Santos da Costa'
print('frase:', frase)
print('frase.split():', frase.split())
print('\'-\'.join(frase):', '-'.join(frase))
print('\'-\'.join(frase.split)):', '-'.join(frase.split()))
input()