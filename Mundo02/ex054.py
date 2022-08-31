from datetime import date
atual = date.today().year
cont = int(0)
menor = int(0)

for i in range(1,8):
    ano = int(input('Em que ano a {}º pessoa nasceu?'.format(i)))
    if (atual - ano) >= 21:

        cont += 1
    else:
        menor +=1
print('{} são maiores de idade'.format(cont))
print('{} são menores de idade'.format(menor))
