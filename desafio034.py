"""
Escreva um programa que pergunte o salário de um funcionáriio e calcule o valor do seu aumento.

Para salários superiores a R$ 1200, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%
"""

salario = float(input('Informe o salário do funcionário '))
if salario <= 1250:
    reajuste = 0.15
else:
    reajuste = 0.10
salario_reajustado = salario + (salario * reajuste)
print(f'O salário de R$ {salario:.2f} foi reajustado para R$ {salario_reajustado:.2f}')