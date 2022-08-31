
cont = 0
cedulas = 50
print('CAIXA ELETRONICO NEW DEV')
valor = int(input('Valor do saque: '))

while True:
    if valor >= cedulas:
        valor -= cedulas
        cont += 1
    else:
        if cont > 0:
            print(f'{cont} de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        cont = 0
        if valor == 0:
            break

