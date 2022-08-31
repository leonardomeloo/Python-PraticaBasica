from random import randint
jogos = {}
jogos['jogador1'] = int(randint(1,6))
jogos['jogador2'] = int(randint(1,6))
jogos['jogador3'] = int(randint(1,6))
jogos['jogador4'] = int(randint(1,6))

for i in sorted(jogos, key= jogos.get, reverse=True):
    print(f'{i}  {jogos[i]}')   
