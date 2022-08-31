total = cont_valor = barato = 0
nomebarato = ''
while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Valor: '))
    op = input('Deseja continuar[S/N]').strip().upper()
    if total == 0:
        nomebarato = nome
        barato = preco

    total += preco

    if preco > 1000:
        cont_valor +=1
    if preco < barato:
        nomebarato = nome
        barato = preco
    if op == 'N':
        break
print(f'Total gasto {total}')
print(f'Produtos com valor acima de 1000:  {cont_valor}')
print(f'Produto mais barato: {nomebarato}')