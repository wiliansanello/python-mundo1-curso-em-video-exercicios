"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia, e R$0,15 por km rodado.
"""

km = float(input('Informe a distância percorrida: '))
dias = int(input('Por quantos dias o carro ficou alugado? '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar pelo aluguel do carro é R$  {:.2f}'.format(valor))