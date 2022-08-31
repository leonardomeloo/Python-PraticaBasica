'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = 1
mais = 11
total = 0
cont = 10
while mais != 0:
    total += mais
    while termo <= total:
        print(primeiro + ((termo-1)*razao), end=' -> ')
        termo+=1
    mais = int(input('Deseja quantos termos a mais?'))
    cont += mais
print('FIM, foram mostrados um total de {} termos!'.format(cont))