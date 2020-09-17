print('=' * 10, 'PROGRAMA TRIÂNGULOS', '=' * 10)
#eval converte para INT ou FLOAT dependendo do valor entrado
a = eval(input('Lado A: '))
b = eval(input('Lado B: '))
c = eval(input('Lado C: '))
if(a < b + c and b < a + c and c < a + b):
    if(a == b and b == c):
        print('É um triângulo equilátero!')
    elif(a == b or a == c or b == c):
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('Os lados informados não formam um triângulo!')
input()
