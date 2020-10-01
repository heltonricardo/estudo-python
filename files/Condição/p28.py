a = int(input('Entre o valor para A: '))
b = int(input('Entre o valor para B: '))
r = a + b
if(r > 10 and r < 20):
    print('{} está entre 10 e 20'.format(r))
else:
    print('{} não está entre 10 e 20'.format(r))
input()
