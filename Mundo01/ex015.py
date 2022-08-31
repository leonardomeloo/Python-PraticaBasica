dia = float(input('Quantos dias de aluguel do carro: '))
km = float(input('Digite a quantidade de Km percorrido pelo carro: '))
valor = (dia*60) + (km*0.15)

print('Valor total do alguel foi de: {:.2f}'.format(valor))