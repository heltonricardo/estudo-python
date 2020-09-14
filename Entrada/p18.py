p_aumento = 15
salario = float(input('Entre valor do salario: '))
novo_salario = salario + salario * (p_aumento / 100)
print('Novo salário ({}% de aumento): R$ {:.2f}'.format(p_aumento, novo_salario))
input()
