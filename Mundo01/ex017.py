import math
co = float(input('Cateto Oposto:'))
ca = float(input('Cateto Adjacente:'))

r = math.hypot(co,ca)

print('Valor da hipotenusa é de: {:.2f}'.format(r))