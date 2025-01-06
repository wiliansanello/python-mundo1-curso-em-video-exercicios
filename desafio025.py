"""Crie um programa que leia o nome de uma pessoa e diga se tem SILVA no nome"""

nome = input('Digite o nome completo: ')
print('Há o nome SILVA no nome? {}'.format('SILVA' in nome.upper()))