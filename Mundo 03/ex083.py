'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
expressao = input('Digite a expressão: ')
cont1 = 0
cont2 = 0
for i in expressao:
    if i == '(':
        cont1+=1
    if i == ')':
        cont2+=1
if cont1 == cont2:
    print('Essa expressão é válida!')
else:
    print('Expressão inválida!')