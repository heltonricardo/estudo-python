print('Entre expressão entre parênteses:')
e = str(input()).strip()
p = []
for i in e:
    if i == '(':
        p.append('(')
    elif i == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Parênteses foram usados corretamente.')
else:
    print('Parênteses não foram usados corretamente.')
input()
