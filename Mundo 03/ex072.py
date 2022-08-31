numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte',)
while True:
    escolha = int(input('Digite um número de 0 a 20:'))
    if 0<= escolha <= 20:
        print(f'{numeros[escolha]}')
        op = input('Deseja sair?[S/N]').upper()
        if op == 'S':
            break
        elif op == 'N':
            continue
