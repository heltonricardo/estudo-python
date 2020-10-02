num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Entre um valor de 0 a 20: '))
    if 0 <= n <= 20: break
    print('Erro!', end=' ')
print(f'Você digitou o número {num[n]}')
input()
