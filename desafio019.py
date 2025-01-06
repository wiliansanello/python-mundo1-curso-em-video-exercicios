"""
Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o  nome
deles e escrevendo o nome do escolhido.
"""
from random import choice

aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('Qual o nome do terceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')
escolhido = choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno escolhido foi {}'.format(escolhido))