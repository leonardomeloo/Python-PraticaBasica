nota1 = float(input('Digite a nota da AV1:'))
nota2 = float(input('Digite a nota da AV2:'))
media = (nota1+nota2)/2

if media < 5:
    print('REPROVADO')
elif media > 5 and media <=6.9:
    print('Recuperação')
else:
    print('APROVADO')
