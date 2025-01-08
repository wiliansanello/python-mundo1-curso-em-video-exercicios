"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro maior é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais
"""

num1 = int(input('Digite o primeiro número '))
num2 = int(input('Digite o segundo número '))

if num1 > num2:
    print('\033[32mO primeiro número é maior')
elif num2 > num1:
    print('\033[34mO segundo número é maior')
else:
    print('\033[33mNão existe valor maior, os dois são iguais')