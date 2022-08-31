from datetime import datetime
ficha = {}
ficha['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.now().year - ano_nascimento
ficha['carteira_trabalho'] = int(input('Número Carteira de trabalho(0 não tem): '))
if ficha['carteira_trabalho'] != 0:
    ficha['ano_contratacao'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['ano_contratacao'] + 35) - datetime.now().year)
for k,v in ficha.items():
    print(f'{k}: {v}')
