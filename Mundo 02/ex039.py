from datetime import date
from math import modf

ano = int(input('Qual ano você nasceu:'))
atual = date.today().year
idade = atual - ano

if idade == 18:
    print('Você já deveria ter se alistado.')

elif idade < 18:
    saldo = 18-idade
    print('Falta {} ano(s) para você se alistar'.format(saldo))
else:
    saldo = idade -18
    print('Seu alistamento era para ser feito a {} ano(s) atrás!'.format(saldo))