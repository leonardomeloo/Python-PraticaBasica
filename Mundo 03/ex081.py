'''Crie um programa que vai ler vários números e colocar em uma lista.
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    n = int(input('Digite o Valor:'))
    lista.append(n)
    op = input('Quer continuar?[S/N]').upper()
    if op == 'N':
        break
    else:
        continue
print(len(lista))
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('Não consta na lista informada.')