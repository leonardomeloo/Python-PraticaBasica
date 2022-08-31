agenda = {}
lista = []
while True:
    agenda.clear()
    agenda['nome'] = input('Nome: ')
    while True:
        agenda['sexo'] = input('Sexo[M/F]: ').upper()
        if agenda['sexo'] in 'MF':
            break
        print('ERRO, Digite o valor correto!')
    agenda['idade'] = int(input('Idade: '))
    lista.append(agenda.copy())
    while True:
        saida = input('Deseja continuar[S/N]: ').upper()
        if saida in 'SN':
           break
    if saida == 'N':
        break
    print('Digite S para SIM ou N para NÃO.')
lista = list(agenda)
print(lista)
print(agenda)