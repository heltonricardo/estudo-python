desc = 5
p1 = float(input('Entre o valor do produto: '))
p2 = p1 - (p1 * desc / 100)
print('Valor com {}% de desconto: {:.2f}'.format(desc, p2))
input()
