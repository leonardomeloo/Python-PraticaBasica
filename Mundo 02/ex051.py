#Determinando o Primeiro termo e a razão Construa um programa que faça uma P.A
n = int(input('Digite o primeiro termo:'))
r =  int(input('Digite a razão da PA:'))
cont = n + (10-1)*r
for i in range(n,cont+r,r):
    print(i)