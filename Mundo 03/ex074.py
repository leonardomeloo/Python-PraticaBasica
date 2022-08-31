from random import randint
numeros = ((randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)),(randint(0,10)))
print('Os valores sorteados foram:')
for i in numeros:
    print(f'{i} ', end='')
print(f'\nMaior valor: {max(numeros)}')
print(f'Menor valor {min(numeros)}')

