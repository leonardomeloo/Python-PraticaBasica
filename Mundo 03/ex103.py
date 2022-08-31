#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = '<desconhecido>', gols=0):
    return print(f'O jogador {nome}, marcou {gols} gol(s) no campeonato.')

jogador = input('Nome do jogado: ')
gol = input('Números de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador,gol)


