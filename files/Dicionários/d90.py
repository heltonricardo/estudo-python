aluno = {}
aluno['nome'] = input('Nome...: ')
aluno['media'] = float(input('Média..: '))
if aluno['media'] >= 6: aluno['situacao'] = 'Aprovado'
else: aluno['situacao'] = 'Reprovado'

print()
for v, k in aluno.items(): print(f'{v} é {k}')
