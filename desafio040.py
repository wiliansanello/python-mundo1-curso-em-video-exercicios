"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

- Média abaixo de 5.0 = REPROVADO
- Média entre 5.0 e 6.9 = RECUPERAÇÃO
- Média entre 7.0 ou superior = APROVADO
"""

nota1 = float(input('Informe a primeira nota '))
nota2 = float(input('Informe a segunda nota '))
media = (nota1+nota2)/2

if media < 5:
    print('\033[1;31mREPROVADO!')
elif media >= 5.0 and media <=6.9:
    print('\033[1;33mRECUPERAÇÃO!')
else:
    print('\033[1;32mAPROVADO!')
print('\033[1;37mSua média final foi {}'.format(media))