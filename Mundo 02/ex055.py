maior = float(0)
menor = float(99999999999999999999999999)
for i in range(1,6):
    peso = float(input('Digite o Peso:'))
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print(maior,menor)
