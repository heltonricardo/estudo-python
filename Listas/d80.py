val = []
for i in range(5):
    n = int(input('Entre valor inteiro: '))
    if i == 0 or n >= val[-1]:
        val.append(n)
    else:
        for j in range(len(val)):
            if n <= val[j]:
                val.insert(j, n)
                break
print('Lista ordenada usando insert:', val)
