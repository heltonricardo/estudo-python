x = 9

print('X no programa principal:', x)

def valores():
    x = 7

    def valor1():
        global x
        x = 1
        y = 2
        print('Sub-rotina valor1. X = {} e Y = {}'.format(x, y))

    valor1()
    print('Sub-rotina valores(). X = {}'.format(x))

    def valor2():
        nonlocal x
        x = 3
        y = 4
        print('Sub-rotina valor2. X = {} e Y = {}'.format(x, y))

    valor2()
    print('Sub-rotina valores() depois de valor2(). X = {}'.format(x))
valores()
input()
