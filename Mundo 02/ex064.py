n = 0
soma = 0
cont = 0
while n !=999:
    n = int(input('Digite um nume[999 para parar]:'))
    if n != 999:
        soma +=n
        cont +=1
    else:
        print('Foram digitados {}, a soma deles é igual a {}!'.format(cont,soma))