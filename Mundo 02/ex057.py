n = 2
while n != 0:

    print('Digite seu sexo [M/F]:')
    sexo = input().upper()

    if sexo == 'M':
        n = 0
        print('Sexo Masculino registrado')
    elif sexo == 'F':
        print('Sexo Feminino registrado')
        n = 0


    else:
        print('Sexo inválido, por favor digite novamente.')
        print('M -> Masculino\nF -> Feminino')