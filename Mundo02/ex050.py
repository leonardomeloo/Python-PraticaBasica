#Soma de 6 números pares
soma = 0
for n in range(0,6,1):
    num = int(input("Digite um número par:"))
    if num%2 == 0:
       soma += num
print(soma)
