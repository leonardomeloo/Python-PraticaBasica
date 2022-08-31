import emoji
l1 = float(input('Primeiro lado do triângulo:'))
l2 = float(input('Segundo lado do triângulo:'))
l3 = float(input('Terceiro lado do triângulo:'))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 +l3 > l2:
    print('PODE SER FORMADO UM TRIANGULO')
else:
    print('Bad News!')