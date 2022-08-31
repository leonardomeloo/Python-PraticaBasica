cont_idade = cont_homens = cont_mulheres = 0
while True:
    print('CADASTRO GERAL')
    idade = int(input('Digite a idade da pessoa cadastrada:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('sexo[M/F]:').strip().upper()
    op = ' '
    while op not in 'SN':
        op = input('Deseja continuar?[S/N]').strip().upper()

    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres +=1
    if op == 'N':
        break

print(f'Pessoas com mais de 18: {cont_idade}')
print(f'Total de Homens: {cont_homens}')
print(f'Total de Mulheres até 19 anos: {cont_mulheres}')

