l = float(input('Entre a largura da parede em metros.: '))
a = float(input('Entre a altura da parede em metros..: '))
area = l * a
tinta = (area / 2)
print()
print('Área da parede......: {:.3f} m²'.format(area))
print('Quantidade de tinta.: {} litros'.format(tinta))
input()
