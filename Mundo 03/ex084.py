lista = []
tabela = []
maior = menor = 0
lista_maior_peso = []
lista_menor_peso = []
while True:
    lista.append(input('Nome:'))
    lista.append(float(input('Peso:')))
    if len(tabela) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    tabela.append(lista[:])
    lista.clear()
    op = input('Digite N para sair:').upper()
    if op == 'N':
        break
for peso in tabela:
    if peso[1] == maior:
        lista_maior_peso.append(peso[0])
    if peso[1] == menor:
        lista_menor_peso.append(peso[0])


print(f'Total de Pessoas é de {len(tabela)}')
print(f'O maior peso foi de {maior}kg, referente a: {lista_maior_peso}')
print(f'O menor peso foi {menor}kg, de: {lista_menor_peso}')
