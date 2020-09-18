n = int(float(input('Entre o valor para tabuada: ')))
print()
for i in range(1, 11):
    print('{:3} x {:2} = {:3}'.format(n, i, n * i))
input()
