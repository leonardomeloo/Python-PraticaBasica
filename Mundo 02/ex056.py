media = 0
maior = 0
hvelho = ''
contm = 0
for i in range(1, 5):
    print('----{}º PESSOA ----'.format(i))
    nome = input('Nome:').upper()
    idade = int(input('Idade:'))
    sexo = input('Sexo(M ou F:)').upper()
    media += idade
    print(media)
    if sexo == 'M' and idade > maior:
        hvelho = nome
    elif idade < 20 and sexo == 'F':
        contm += 1
print('Media da idade do grupo é de:{}'.format(media/4))
print('Homem mais velhor:{}'.format(hvelho))
print('Mulheres com menos de 20 anos:{}'.format(contm))