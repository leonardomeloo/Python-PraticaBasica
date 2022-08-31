frase = input('Digite a frase:').strip().lower()
n = frase.count('a')
oc1 = []
ult = 0
for x in range(0,len(frase)):
    if frase[x] == 'a':
        oc1 += [x]



print(oc1)
print('Quantidade de (a) na frase é:{}, Primeira posição:{}, última posição:{}'.format(n,oc1[0],oc1[-1]))