s = 0
for i in range(6):
    n = int(float(input('({}) Entre um valor: '.format(i + 1))))
    if n % 2 == 0:
        s += n
print('Soma dos pares entrados:', s)
input()
