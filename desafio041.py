"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import datetime

entrada=str(input('Informe a data de nascimento do nadador '))
data_nascimento = datetime.strptime(entrada, '%d/%m/%Y')
data_atual = datetime.today()
idade = data_atual.year - data_nascimento.year

# Verifica se o dia e o mês da data de nascimento já chegaram ou passaram da data atual
if (data_atual.month, data_atual.day) < (data_nascimento.month, data_atual.day):
    idade -= 1

print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
else:
    print('Categoria SÊNIOR')