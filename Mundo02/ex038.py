#Numero maior
n1 = int(input('Digite o primeiro Numero:'))
n2 = int(input('Digite o segundo numero:'))

if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}'.format(n1,n2))
elif n2 > n1:
    print('O Segundo valor {} é maior que o Primeiro {}'.format(n2, n1))
else:
    print('Eles são iguais')