'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
#An = a1 + (n-1)*R
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = 1
while termo != 11:
    print(primeiro + ((termo-1)*razao), end=' -> ')
    termo+=1
print('FIM')