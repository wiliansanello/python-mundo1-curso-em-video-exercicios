"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO
"""

cidade = input('Digite o nome da cidade onde você mora ').strip()
#dividido = cidade.split()
#print('Sua cidade começa com SANTO? {}'.format('SANTO' in dividido[0].upper()))

# O trecho do nome procurado é sempre o mesmo, está no início e tem 5 letras, sendo possível usar a forma abaixo
print('O nome da cidade digitada inicia com SANTO? {}'.format(cidade[0:5].upper() == 'SANTO'))