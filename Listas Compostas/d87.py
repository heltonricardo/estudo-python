l = []
for i in range(3):
    l.append([])
    for j in range(3):
        print(f'Entre valor para [{i}][{j}]:', end=' ')
        l[i].append(int(input()))

par = 0
ter = 0
for i in range(3):
    for j in range(3):
        print(f'[{l[i][j]:^5}]', end='')
        if l[i][j] % 2 == 0: par += l[i][j]
        if j == 2: ter += l[i][j]
    print()

print('A) Soma dos pares .......................:', par)
print('B) Soma dos valores na terceira coluna ..:', ter)
print('C) Maior valor da segunda coluna ........:', max(l, key=lambda x: x[1])[1])
input()
