"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até 200Km e R$ 0,45 para viagens mais longas.
"""

distancia = float(input('Qual a distância da viagem que irá fazer? '))

#passagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    passagem = 0.5
else:
    passagem =  0.45
valor_viagem = distancia * passagem

print('O valor da viagem será R$ {:.2f}'.format(valor_viagem))