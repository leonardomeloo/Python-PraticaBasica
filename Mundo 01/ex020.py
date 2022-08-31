from random import choice,shuffle
n1 = input('Primeiro pessoa:')
n2 = input('Segunda:')
n3 = input('Terceira:')
n4 = input('Quarta:')

lista = [n1,n2,n3,n4]
shuffle(lista)
print('Ordem de apresentação: {}'.format(lista))
