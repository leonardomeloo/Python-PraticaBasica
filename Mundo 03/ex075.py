numeros = (int(input('Primeiro numero:')),int(input('Segundo:')),int(input('Terceiro:')),int(input('Quarto:')))
pares = []
for i in range(0,len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
print(f'Valores: {numeros}')
print(f'Quantas vezes apareceu o valor [9]: {numeros.count(9)}')
if 3 in numeros:
    print(f'Em que posição foi digitado o primeiro valor 3: {numeros.index(3)}')
else:
    print('O valor 3 não foi incluido nessa passagem.')
print(f'Quais foram os números pares:{pares}')
