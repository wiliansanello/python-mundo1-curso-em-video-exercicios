"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from playsound import playsound
from time import sleep

print(' '*50 + '-'*20)
print(' '*50 + 'JOGO DA ADIVINHAÇÃO')
print(' '*50 + '-'*20)

numero=int(input('Adivinhe em qual número de 0 a 5 eu estou pensando '))

print('Resposta saindo em ... 3')
sleep(1)
print('2')
sleep(1)
print('1')

if numero < 0 or numero > 5 : #Checa se o número está entre 0 e 5
    print('Esse número é maior que 5 e/ou menor que zero. Por favor, tente novamente')
else:
    resultado = randint(0,5) # Computador "pensa" no número

    print('O número sorteado foi {1}, e você escolheu {0}'.format(numero, resultado))

    if numero==resultado:
        print('Parabéns. Você acertou!')
        playsound("desafio028-acertou.mp3")
    else:
        print('Que pena, você errou. Tente novamente!')
        playsound("desafio028-errou.mp3")