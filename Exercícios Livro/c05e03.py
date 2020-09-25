def iop(n):
    if (n % 2 == 0):
        return 'par'
    else:
        return 'ímpar'

while (True):
    num = int(float(input('Entre um valor natural: ')))
    if (num > 0): break

print('O valor {} é'.format(num), iop(num))
input()
