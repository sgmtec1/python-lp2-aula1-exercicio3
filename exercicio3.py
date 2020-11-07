''' Escreva um programa que solicite o salário atual de um funcionário e calcula o valor do salário com
um reajuste de aumento, sendo que:
- Caso o salário atual seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
- Caso contrário, o funcionário receberá 15% de aumento.
'''
salario = float(input("Salário do Funcionário: "))
if salario > 2000:
    novo_salario = salario * 1.07
    print("Novo Salário:", novo_salario)
else:
    novo_salario = salario * 1.15
    print("Novo Salário:", novo_salario)
