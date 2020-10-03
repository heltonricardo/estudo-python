brasil = list()
leitura = dict()
for i in range(3):
    leitura['uf'] = input('Nome do estado...: ')
    leitura['sigla'] = input('Sigla do estado..: ')
    print()
    brasil.append(leitura.copy())
print(brasil)
