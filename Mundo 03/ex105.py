#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas; – A maior nota; – A menor nota; – A média da turma; – A situação (opcional)

def notas(*num, sit=False):
    dic = {}
    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    dic['media'] = sum(num)/len(num)
    if sit == True:
        if dic['media'] < 7:
            dic['situação'] = 'Ruim'
        elif 7<= dic['media'] <=7.9  :
            dic['situação'] = 'Razoável'
        else:
            dic['situação'] = 'Boa'
    return dic

resposta = notas(8,8,8,sit=True)
print(resposta)