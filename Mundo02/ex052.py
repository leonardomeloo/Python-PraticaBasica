n = int(input('Digite o Número:'))
cont = 0
a =[]
for i in range(1,n+1):
    if n % i == 0:
        cont +=1
        a.append(i)
if cont == 2:
    print('O número {} é primo.'.format(n))
else:
        print('O número {} não é um número primo.'.format(n))
        print('Ele foi dividido por: {}'.format(a))