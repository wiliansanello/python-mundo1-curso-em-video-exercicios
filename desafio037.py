"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

1 -  para binário
2 - para octal
3 - para hexadecimal
"""

numero = int(input('Digite um número para realizarmos a conversão '))
base = int(input('Digite a opção de conversão da base \n1 - Binário \n2 - Octal \n3 - Hexadecimal\n'))

print(f'O número digitado foi o {numero}')
if base == 1:
    print(f'Convertido para binário: {bin(numero)}')
elif base == 2:
  print(f'Convertido para Octal: {oct(numero)}')
elif base == 3:
  print(f'Convertido para Hexadecimal: {hex(numero)}')

