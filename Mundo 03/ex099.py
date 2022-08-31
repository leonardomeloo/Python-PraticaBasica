def maior(*num):
    lista = []
    for i in num:
        lista.append(i)
    return max(lista)

print(maior(2,9,4,5,7,1))
print(maior())