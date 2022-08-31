import math
ag = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tg = math.tan(math.radians(ag))
print('Seno: {:.2f} === Cos: {:.2f} === Tg: {:.2f} ==='.format(seno,cos,tg))
