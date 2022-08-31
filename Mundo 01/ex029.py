velocidade = float(input('Digite a velocidade do carro:'))

if velocidade <= 80:
    print('Velocidade permitida.')
else:
   # multa = float(velocidade-80)*7
    print('Você ultrapassou o limite de velocidade. Multa no valor de:R$ {:.2f}'.format((velocidade-80)*7))