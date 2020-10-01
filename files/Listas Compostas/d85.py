num = [[], []]
for i in range(7):
    n = int(input('Entre valor par ou ímpar: '))
    if n % 2 == 0: num[0].append(n)
    else: num[1].append(n)
print('Pares ....:', sorted(num[0]))
print('Ímpares ..:', sorted(num[1]))
input()
