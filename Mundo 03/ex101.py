def voto(ano_Nascimento):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano_Nascimento
    if idade <= 16:
        return print(f'Com {idade} ano: Você não pode votar')
    elif idade >=16 and idade < 18 or idade > 65:
        return print(f'Com {idade} ano: O voto é Opcional!')
    else:
        return print(f'Com {idade} anos: O voto é OBRIGATÓRIO!')

ano = int(input('Qual ano você nasceu: '))
voto(ano)
