dados = {}
gols = []
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas jogou: '))
for i in range(0,partidas):
    gol = int(input(f'Gols na partida {i+1}: '))
    gols.append(gol)
dados['gols'] = gols
dados['total_gols'] = sum(gols)
print('=-' * 30)
print(dados)
print('=-' * 30)
for k,v in dados.items():
    print(f'O campo {k}, tem valor {v}: ')
print('=-' * 30)
print('Gols por cada jogo!')
for i,c in enumerate(dados['gols']):
    print(f'Partida {i}, o jogador fez {c} gols')