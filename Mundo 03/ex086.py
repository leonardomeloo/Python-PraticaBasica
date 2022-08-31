matriz =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        n = int(input(f'Digite o valor na posicão {i,j}:'))
        matriz[i][j] = n
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}] ', end='')
    print()