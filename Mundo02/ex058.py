from random import randint
n = randint(0,10)
cont = 0
op = 0
while op != 1:
    escolha = int(input('Qual sua escolha de 0 a 10:'))
    if escolha > n:
        print('Menos...')
        cont += 1
    elif escolha < n:
        print('Mais...')
        cont += 1
    else:
        cont +=1
        op = 1
print('Você acertou com {} tentativas!!!'.format(cont))