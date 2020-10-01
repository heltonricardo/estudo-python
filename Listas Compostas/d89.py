alunos = []
dados = []
while True:
    dados.append(str(input('Nome ....: ')))
    dados.append(float(input('Nota 1 ..: ')))
    dados.append(float(input('Nota 2 ..: ')))
    alunos.append(dados[:])
    dados.clear()
    c = str(input('Continuar? [S] para Sim: '))
    print()
    if not c in 'Ss': break
    
for i, a in enumerate(alunos):
    m = (a[1] + a[2]) / 2
    print(f'Nº {i + 1:2} Nome: {a[0]:.<15} Média: {m}')

while True:
    n = int(input('\nEntre número do aluno para mostrar notas ou [0] para sair: '))
    if n == 0: break
    print('Notas de', alunos[n - 1][0] +  ':', str(alunos[n - 1][1]), str(alunos[n - 1][2]))
input()
