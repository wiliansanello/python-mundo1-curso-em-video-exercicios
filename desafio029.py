"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado.

A multa vai custar R$ 7,00 por cada km acima do limite.
"""

velocidade=float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Seu carro está em velocidade {} km/h, {} km acima do limite permitido de 80 km/h. Você foi multado em R$ {:.2f}, '
          'sendo que cada Km excedido vale R$ 7,00'.format(velocidade,(velocidade-80), multa))
print('Dirija com segurança, boa viagem')