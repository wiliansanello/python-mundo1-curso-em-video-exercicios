"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m²
"""
largura = float(input('Qual a largura em metros da parede? '))
altura = float(input('Qual a altura em metros da parede? '))
area = largura*altura
print('A área da parede é {} m². Você precisará de {} litros de tinta para fazer a pintura.'.format(area, area/2))
