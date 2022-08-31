boletim = {}
boletim['nome'] = str(input("Nome do Auluno: "))
boletim['media'] = float(input(f'Media de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Reprovado'

print(f'Aluno: {boletim["nome"]}, Media: {boletim["media"]}, situação:{boletim["situacao"]}',end=' ')
