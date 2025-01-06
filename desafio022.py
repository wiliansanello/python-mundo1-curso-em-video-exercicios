"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras no total (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""
nome = str(input('Digite o nome completo: '))
dividido = nome.split()
juntado = ''.join(dividido)
print('Nome completo em maiúsculas: {}'.format(nome.upper()))
print('Nome completo em minúsculas: {}'.format(nome.lower()))
print('Total de letras no nome: {}'.format(len(juntado)))
print('Contando as letras diretamente do nome digitado: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras no primeiro nome: {}'.format(len(dividido[0])))
print('Contando letras do primeiro nome diretamente do nome digitado: {}'.format(nome.find(' ')))
