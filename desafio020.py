"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
"""
from random import shuffle
aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem dos alunos que vão apresentár os trabalhos é ' + ', '.join(lista))
