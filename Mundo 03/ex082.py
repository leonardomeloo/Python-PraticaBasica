''' Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
 Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite o valor desejado: ')))
    op = input('Para sair digite S')
    if op in 'Ss':
        break

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Lista Completa: {lista}')
print(f'Lista dos numeros pares: {pares}')
print(f'Listas dos números impares: {impares}')
