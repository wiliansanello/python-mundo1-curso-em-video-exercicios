#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

numero = int(input('Informe um número para descobrir se ele é par ou ímpar: '))
if numero % 2 == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))
