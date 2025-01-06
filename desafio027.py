"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex.: Ana Maria de Souza
primeiro=Ana
último=Souza
"""

nome = str(input('Digite o nome completo: ')).strip()
dividido = nome.split()
print('Primeiro nome: {} \nÚltimo nome: {}'. format(dividido[0], dividido[len(dividido)-1]))