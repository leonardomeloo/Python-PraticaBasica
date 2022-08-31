'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
 ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = []
op = 's'
while True:
    n = (int(input('Digite um valor: ')))
    if n in numeros:
        print(f'O numero {n} já existe na lista')
    else:
        numeros.append(n)
        print(numeros)
    op = input('Quer continuar?[S/N]: ').upper()
    if op in 'Nn':
        break
    elif op in 'Ss':
        continue
numeros.sort()
print(numeros)
