a = eval(input('Entre um valor para A: '))
b = eval(input('Entre um valor para B: '))
#operador ternário: var = SIM if(condição) else NÃO
r = a if(a > b) else b
ip = 'par' if(r % 2 == 0) else 'ímpar'
print('O maior valor informado é {}. É um valor {}.'.format(r, ip))
input()
