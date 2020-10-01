def fatr(n):
    if (n == 0):
        return 1
    else:
        return n * fatr(n - 1)

while (True):
    n = int(float(input('Entre valor para fatorial: ')))
    if (n >= 0 and n <= 990): break

print('O fatorial de {} é {}'.format(n, fatr(n)))
input()
