#Refazer a tabuada do ex009 com for
n = int(input('Digite um número para gerar sua Tabuáda:'))
for i in range(1,11):
        print('{} x {:2} = {}'.format(n,i,(n*i)))



