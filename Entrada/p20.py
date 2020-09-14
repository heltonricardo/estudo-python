km = float(input('Kilômetros rodados.: '))
dias = float(input('Dias alugados......: '))
preço = 60 * dias + km * 0.15
print('\nValor a pagar: R$ {:.2f}'.format(preço))
input()
