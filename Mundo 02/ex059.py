n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
op = 0
while op != 5:
    op = int(input('Qual sua opção =>'))
    if op == 1:
        print('A soma de {} + {} = {}'.format(n1,n2,n1+n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif op == 3:
        print(max(n1,n2))
    elif op == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif op == 5:
        print('Até a Proxima!')
    else:
        print('OPÇÃO INVÁLIDA!')
