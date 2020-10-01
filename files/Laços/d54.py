from datetime import datetime
x = datetime.now()
n = []
for i in range(7):
    n.append(int(input('Entre {}º/7 ano de nascimento: '.format(i + 1))))
for i in range(7):
    print('{}º: tem {} anos e é'.format(i + 1, x.year - n[i]), end=' ')
    if x.year - n[i] >= 18:
        print('maior de idade.')
    else:
        print('menor de idade.')
