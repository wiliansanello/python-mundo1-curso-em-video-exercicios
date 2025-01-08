"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ainda falta tempo para ele alistar ao serviço militar, e quanto tempo
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

"""
from datetime import datetime

entrada = str(input('Qual sua data de seu nascimento? '))
data_nascimento = datetime.strptime(entrada,"%d/%m/%Y")
ano_atual = datetime.today()
idade = ano_atual.year - data_nascimento.year
meses_idade = ano_atual.month - data_nascimento.month

#Checa se o dia e o mês do nascimento já chegaram
if (ano_atual.month, ano_atual.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

if idade < 0:
    print('Por favor, informe um ano válido.')
elif idade < 18:
    print(f'A idade para alistamento é 18 anos, e você tem {idade} anos. Ainda faltam {18 - idade} anos para você poder se alistar.')
elif idade == 18:
    print(f'Você já pode se alistar')
else:
    print(f'Já passou do tempo de você se alistar')

