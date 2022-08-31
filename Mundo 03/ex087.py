matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
terceira_coluna = []
segunda_linha = []
for linha in range(0,3):
    for coluna in range(0,3):
        n = int(input(f'Digite o valor para posição {linha,coluna}:'))
        matriz[linha][coluna] = n
        if n % 2 == 0:
            pares.append(n)
        if coluna == 2:
            terceira_coluna.append(n)
        if linha == 1:
            segunda_linha.append(n)


for mostrar_linha in range(0,3):
    for mostrar_coluna in range(0,3):
        print(f'{matriz[mostrar_linha][mostrar_coluna]:^5}',end='')
    print()
print('-='*20)
print(f'A soma dos pares é: {sum(pares)}')
print(f'Soma da terceira coluna é de: {sum(terceira_coluna)}')
print(f'O maior valor é o: {max(segunda_linha)}')
print('-=' *20)


