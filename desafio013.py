"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario=float(input('Informe o salário atual do funcionário: '))
salario_reajustado = salario+(salario*0.15)
print('Com o aumento, o salário desse funcionário passa de R$ {:.2f} para R$ {:.2f}'.format(salario, salario_reajustado))