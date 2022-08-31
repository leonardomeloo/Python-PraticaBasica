def escreva(txt):
    print('=' * len(txt))
    print(f'{txt}')
    print('='*len(txt))
texto = input('Digite o texto:\n')
print(escreva(texto))