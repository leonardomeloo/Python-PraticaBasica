lista = []
while True:
    dados = []
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = float(nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    dados.clear()
    op = input('Deseja Continuar?[S/N]')
    if op in 'nN':
        break
print(lista)
for i, a in enumerate(lista):
    print(f'{i+1} {a[0]} media {a[2]}')
while True:
    op = str(input('Mostrar nota de qual Aluno? (999) for STOP: '))
    if op == '999':
        break
    for op in lista:
        print(op[1])


