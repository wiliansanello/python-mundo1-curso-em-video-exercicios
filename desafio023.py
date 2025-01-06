"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Exemplo: Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

numero = int(input("Digite um número: "))
num = str(numero)
print("""
unidade: {}
dezena: {}
centena: {}
milhar: {}
""".format(num[3], num[2], num[1], num[0]))