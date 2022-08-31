from datetime import datetime
#atual = datetime.today().year '''Pega o ano atual, de acordo com a data do pc'''

ano = int(input("ano: "))
d = datetime.today().strftime('%d/%m/%Y')
data = d.split('/')


anov = int(data[2]) - ano

if anov < 9:
    print('MIRIM')
elif anov >= 9 and anov < 14:
    print('Infantil')
elif anov >= 14 and anov < 19:
    print('Junior')
elif anov >= 19 and anov < 20:
    print('Senior')
else:
    print('MASTER')