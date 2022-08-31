print('1-À vista(10% de desconto!)\n2-À bista no cartão(5% de desconto)')
print('3-Em até 2x no cartão\n4-3x no cartão(20% de juros)')
op = int(input())
preco = float(input('Valor do produto:'))


if op == 1:
    preco = preco - (preco * 0.1)
    print('Valor ficou de {}R$'.format(preco))
elif op == 2:
    preco = preco - (preco * 0.05)
    print('Valor ficou de R${}'.format(preco))
elif op == 3:
    print('Valor ficou de R${}'.format(preco))
    print('Valor da parcela ficou de R${}, em 2x'.format(preco/2))
elif op == 4:
    preco = preco + (preco * 0.2)
    print('Valor ficou de R${}'.format(preco))
    print('Valor da parcela ficou de R${}, em 3x'.format(preco / 3))
else:
    print('Digite uma opção valida!')