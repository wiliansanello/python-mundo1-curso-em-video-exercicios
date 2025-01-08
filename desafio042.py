"""Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: todos os lados diferentes
"""

lado1 = float(input('Informe o valor da primeira reta '))
lado2 = float(input('Informe o valor da segunda reta '))
lado3 = float(input('Informe o valor da terceira reta '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print(f'Ótimo. As retas de valores {lado1}, {lado2} e {lado3} formam um triângulo ', end = ' ')
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('ISÓSCELES')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('ESCALENO')
else:
    print(f'Que pena. As retas de valores {lado1}, {lado2} e {lado3} não forma um triângulo.')