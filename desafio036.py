"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado.
"""
from math import ceil

valor_casa=float(input('Digite o valor da casa que deseja comprar: '))
salario=float(input('Digite seu salário: '))
anos=int(input('Em quantos anos pretende pagar o imóvel?: '))

prestacao = valor_casa/(anos*12)
print(f'Seu salário é de R$ \033[33m{salario:.2f}\033[m, a casa que deseja comprar vale \033[32m{valor_casa:.2f}\033[m. Pagando em \033[36m{anos}\033[m anos, as parcelas serão de R$ {prestacao:.2f}')
if (prestacao/salario) <= 0.3:
    print(f'\033[1;32mÉ possível fazer o financiamento da casa!\033[m')
else:
    print(f'\033[1;31mLamentamos, mas não é possível fazer o financiamento da casa!\033[m')
