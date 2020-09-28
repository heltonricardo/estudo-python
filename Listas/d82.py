val = list()
while True:
    n = int(input('Entre um valor. [0] para finalizar: '))
    if n == 0: break
    val.append(n)
p = [x for x in val if x % 2 == 0]
i = [x for x in val if x % 2 != 0]
print()
print('Lista Total ....:', val)
print('Lista Pares ....:', p)
print('Lista Ímpares ..:', i)
input()
