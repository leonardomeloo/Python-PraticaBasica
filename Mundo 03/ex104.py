#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaint(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            n = int(n)
            break
        print('\033[0;31mNúmero digitado incorreto. Digite corretamente!\033[m')
    return n


n = leiaint('Digite um numero inteiro:')
print(f'O número digitado foi {n}')