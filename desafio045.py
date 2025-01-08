#Crie um programa que faça o computador jogar jokenpô com você
from random import randint

print('='*20)
print('JOKENPÔ')
print('='*20)
escolha = int(input('Escolha sua opção: \n0 - pedra \n1 - papel \n2 - tesoura \n'))

escolha_computador = randint(0,2)
print(f'Você escolheu {escolha}, e eu escolhi {escolha_computador}')
if escolha == escolha_computador:
    print('Empate.')

elif (escolha == 0 and escolha_computador == 1) or (escolha == 1 and escolha_computador == 0):
    print('Pedra embrulha papel.', end ='')
    if escolha == 0:
        print('Você venceu!')
    else:
        print('Eu venci!')

elif (escolha == 0 and escolha_computador == 2) or (escolha == 2 and escolha_computador == 0):
    print('Tesoura corta papel', end='')
    if escolha == 0:
        print('Eu venci!')
    else:
        print('Você venceu!')

elif (escolha == 1 and escolha_computador == 2) or (escolha == 2 and escolha_computador == 1):
    print('Pedra quebra tesoura', end='')
    if escolha == 1:
        print('Você venceu')
    else:
        print('Eu venci!')