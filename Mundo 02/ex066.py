cont = soma = 0
while True:
    n = int(input('Digite o número:'))
    if n == 999:
        break
    cont+=1
    soma += n
print(f'Foram digitados {cont} números\nA soma é igual à {soma}')