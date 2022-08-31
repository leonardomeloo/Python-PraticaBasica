#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
for i in range(0,5):
    numero = int(input('Digite o numero:'))
    numeros.append(numero)
print(f'O maior numero digitado foi: {max(numeros)}, e sua posição é {numeros.index(max(numeros))}')
print(f'O menor numero  digitado foi: {min(numeros)}, e sua posição é {numeros.index(min(numeros))}')
