"""
Escreva um programa que converta a temperatura em Celsius para Fahrenheit e Kelvin
"""

celsius = float(input('Informe a temperatura em C: '))
kelvin = celsius + 273
fahrenheit = celsius * 1.8 + 32
print('{:.1f} ºC correspondem a {:.1f} ºF e {:.1f} K'.format(celsius, fahrenheit, kelvin))