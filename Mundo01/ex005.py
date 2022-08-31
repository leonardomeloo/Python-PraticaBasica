#end = ' ' => Não deixa ter quebra de linha de um print para o outro com o caracter q tiver dentro
#'{:>20}' => Alinhamento para direita
#'{:<20}' => Alinhamento para esquerda
#'{:^20}' => Centraliza
#'{:=^3}' => Centraliza com o caracter antes do ^. Ex: ===Leo===

n1 = int(input('Digite um numero: '))
print('Antecessor: {}, Número escolhido {} e Sucessor: {}'.format(n1-1,n1,n1+1))