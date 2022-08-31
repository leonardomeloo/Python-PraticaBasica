import random
op = int(input('1-Pedra\n2-Papel\n3-Tesoura\n-->'))
op2 = random.randint(1,3)

if op == 1 and op2 == 1:
    print('EMPATE')
elif op == 1 and op2 == 2:
    print('Papel ganha de Pedra! IA WIN!')
elif op == 1 and op2 == 3:
    print('Pedra ganha de Tesoura. Você Venceu!')
elif op == 2 and op2 == 1:
    print('Papel ganha de Pedra! Você venceu!')
elif op == 2 and op2 == 2:
    print('EMPATE')
elif op == 2 and op2 == 3:
    print('Tesoura ganha de Pedra! IA WIN!')
elif op == 3 and op2 == 1:
    print('Pedra ganha para Tesoura! IA WIN!')
elif op == 3 and op2 == 2:
    print('Tesoura ganha de Papel. Você Venceu!')
elif op == 3 and op2 == 3:
    print('EMPATE')