n = int(float(input('Entre um valor inteiro: ')))
sr = int(n ** (1 / 2)) + 1
flag = True
for i in range(2, sr):
    if n % i == 0:
        flag = False
        break
if flag:
    print('O valor entrado é primo')
else:
    print('O valor entrado não é primo')

input()
