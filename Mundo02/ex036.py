salario = float(input("Valor do seu salário:"))
casa = float(input("Valor da Casa:"))
anos = int(input("Quantos anos deseja pagar?"))
anos = anos * 12
parcela = casa/anos

if parcela <= (salario*0.3):
    print("Emprestimo APROVADO")
else:
    print("Emprestimo Negado. A margem exede 30% do salário.")