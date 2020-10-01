l = []
for i in range(3):
    l.append([])
    for j in range(3):
        print(f'Entre valor para [{i}][{j}]:', end=' ')
        l[i].append(int(input()))

for i in range(3):
    for j in range(3):
        print(f'[{l[i][j]:^5}]', end='')
    print()
input()
