"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa
"""
from math import pow, sqrt, hypot
oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = sqrt(pow(oposto,2)+pow(adjacente,2)) # Outra forma de calcular: (oposto ** 2 + adjacente ** 2) ** (1/2)
hip = hypot(oposto, adjacente)
print('Para os valores dos catetos oposto {} e adjacente {}, a hipotenusa é {:.2f}'.format(oposto, adjacente,hipotenusa))
print('Valor da hipotenusa: {:.2f}'.format(hip))
