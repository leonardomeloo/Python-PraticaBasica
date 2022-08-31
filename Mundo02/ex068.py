from random import randint
cont = 0
while True:
    op = input('Escolha PAR ou IMPAR: ').strip().upper()
    n1 = int(input('Escolha um número de 0 a 10: '))
    n2 = randint(0,10)
    resultado = n1+ n2
    if op == 'PAR' and resultado % 2 == 0:
        print(f'Você venceu! Seu número {n1}, número PC {n2} ')
        cont+=1
    elif op == 'IMPAR' and resultado % 2 == 1:
        print(f'Você venceu! Seu número {n1}, número PC {n2} ')
        cont+=1
    else:
        print(f'Você perdeu! Seu número {n1}, número PC {n2} ')
        break
print(f'Vitórias seguidas {cont}')