def fatorial(n):
    fat = 1
    for i in range(2, n + 1):
        fat *= i
    print('Fatorial de {} é {}'.format(n, fat))
    
n = int(float(input('Entre valor para fatorial: ')))
fatorial(n)
input()
