'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numeros = []
for i in range(0,5):
    n = int(input('Digite o valor: '))
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Foi adicionado no final da lista')

    else:
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao,n)
                print(f'Foi inserido na posição {numeros.index(n)}, o numero {n}')
                posicao+=1
                break
            else:
                posicao+=1



print(numeros)