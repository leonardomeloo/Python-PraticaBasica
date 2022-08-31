lista = [[],[]]
for i in range(0,7):
    numero = int(input('Digite o valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'Lista de pares digitados: {lista[0]}')
print(f'Lista de impares digitados:{lista[1]}')
