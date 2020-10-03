from time import strftime
now = int(strftime('%Y'))
dados = {}
dados['nome'] = input('Nome..................: ')
dados['idade'] = now - int(input('Ano de nascimento.....: '))
dados['CTPS'] = int(input('Carteira de Trabalho..: '))
if dados['CTPS'] != 0:
    dados['ano_de_contratacao'] = int(input('Ano de contratacao....: '))
    dados['salario'] = float(input('Salário...............: '))
    dados['idade_que_aposenta'] = dados['idade'] + 45
for v, k in dados.items(): print(f'{v} é igual a {k}')
