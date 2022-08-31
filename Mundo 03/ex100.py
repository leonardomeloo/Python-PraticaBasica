from random import randint
def sorteia(lista):
    for i in range(0,5):
        lista.append(randint(0,10))
def somaPar(lista):
    soma = []
    for i in range(0,len(lista)):

        if lista[i] %2 == 0:
            soma.append(lista[i])
    return sum(soma)
numeros= []
sorteia(numeros)
print(numeros)
print(somaPar(numeros))
