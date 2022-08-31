d = float(input('Distancia em Km:'))

if d <= 200:
    print('valor da viagem:{:.2f}'.format(d*0.5))

else:
    print('valor da viagem:{:.2f}'.format(d * 0.45))