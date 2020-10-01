val = list()
while True:
    n = int(input('Entre um valor. [0] para finalizar: '))
    if n == 0: break
    val.append(n)
print('Quantidade de valores digitados:', len(val))
val.sort(reverse=True)
print('Lista decrescente:', val)
print('Lista possui valor 5?:', 5 in val)
input()
