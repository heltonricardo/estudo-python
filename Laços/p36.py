s = 0
print('Entre dez valores positivos:\n')
for i in range(1, 11):
    n = int(input('{:2}: '.format(i)))
    if (n <= 0):
        print('Valor inserido incorretamente. Programa encerrado!')
        break
    s = s + n
else:
    print('A soma é igual a', s)
input()
