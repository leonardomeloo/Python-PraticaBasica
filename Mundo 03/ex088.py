import random
import time
from time import sleep
quantidade_jogos = int(input('Quantos jogos você deseja fazer? '))


for i in range(0,quantidade_jogos):
    jogo = []
    lista_mega = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                  28,
                  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                  53,
                  54, 55, 56, 57, 58, 59, 60]
    if len(jogo) < 6:
        while len(jogo)< 6:
            n = random.randint(1,60)

            if n in lista_mega and len(jogo) < 6:
                jogo.append(n)
                lista_mega.remove(n)
        time.sleep(1)
        print(jogo)



