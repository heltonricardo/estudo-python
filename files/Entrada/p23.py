from math import floor, trunc
n = float(input('Entre um número real: '))
fl = floor(n)
tr = trunc(n)
ca = int(n)
print()
print('FLOOR :: O número {} tem a parte inteira {}.'.format(n, fl))
print('TRUNC :: O número {} tem a parte inteira {}.'.format(n, tr))
print('CAST  :: O número {} tem a parte inteira {}.'.format(n, ca))
input()
