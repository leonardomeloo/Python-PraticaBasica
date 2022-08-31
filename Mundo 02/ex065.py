op = 'S'
soma = cont = maior = menor = 0
while op == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if maior < n:
        maior = n
    if cont == 1:
        menor = maior
    if menor > n:
        menor = n

    op = input('Quer continuar? [S/N]:').upper().strip()
print('{} foram digitados e a média foi {}'.format(cont,soma/cont))
print('Maior número digitado {} // Menor número digitado {}'.format(maior,menor))
