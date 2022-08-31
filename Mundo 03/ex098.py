def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo *= -1

    for i in range(inicio,fim,passo):
        print(i,end=' ')

    print('\n')

contador(1,11,1)
contador(10,-1,-2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)