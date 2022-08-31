#Transformar o numero em binário, octal e Hexadecimal. 11001
numero = int(input("Digite o numero: "))
alternativa = int(input("Digite a alternativa:\n 1-Binário\n 2-Octal\n 3-Hexadecimal\n"))

binario = bin(numero)
octa = oct(numero)
hexa = hex(numero)

if alternativa == 1:
    print(binario[2::])
elif alternativa == 2:
    print(octa[2::])
elif alternativa == 3:
    print(hexa[2::])
else:
    print('Escolha a opção correta!\n')
