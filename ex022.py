#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo(sem considerar espaços
#Quantas letras tem o primeiro nome

nome = input("Digite o nome completo:").strip()
nome2=''
print(nome.upper())#O nome com todas as letras maiusculas
print(nome.lower())#O nome com todas as letras minusculas
#print(nome.find(' '))#Quantas letras tem o primeiro nome
nome3 = nome.split(' ')
print(len(nome3[0]))#Quantas letras tem o primeiro nome

espacos = nome.count(' ')
print(len(nome) - espacos)



