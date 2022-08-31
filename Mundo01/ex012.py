item = float(input('Valor do produto: '))
desconto = (item/100)*5
valorf = item - desconto

print('Valor do produto com desconto é de: {:.3f}'.format(valorf))