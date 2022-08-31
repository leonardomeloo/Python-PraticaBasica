import random

n1 = random.randint(1,5)

n2 = int(input('Digite um numero para acertar:'))

if n1 == n2:
    print('Você acertou o valor:')
else:
    print('Você errou, o número escolhido foi:{}'.format(n1))

