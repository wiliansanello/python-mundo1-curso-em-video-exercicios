"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
"""

from math import trunc, floor
num = float(input('Digite um número real: '))
print('A porção inteira de {} é {}'.format(num, trunc(num)))
print('Novamente. A porção inteira de {} é {}'.format(num, floor(num)))
print('Mais uma vez. O número digitado foi {}, e sua parte inteira é {}'.format(num, int(num)))