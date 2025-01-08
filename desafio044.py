"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- A vista: dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

print('O produto vale R$ 100. Escolha abaixo a forma de pagamento: ')
print('1 - A vista dinheiro/cheque')
print('2 - A vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')

condicao = int(input('Informe a condição escolhida: '))
qtd_parcelas = 1

if condicao == 1:
    preco = 100-(100*0.10)
    descricao = 'a vista dinheiro/cheque'
elif condicao == 2:
    preco = 100-(100*.05)
    descricao = 'a vista no cartão'
elif condicao == 3:
    qtd_parcelas = 2
    preco = 100
    descricao = '2x no cartão'
    parcela = preco/2
elif condicao == 4:
    qtd_parcelas = int(input('Em quantas parcelas deseja pagar? '))
    if qtd_parcelas >=3:
        parcela = 100/qtd_parcelas
    preco = parcela + (parcela * 0.20)
    descricao = '3x ou mais no cartão'

print(f'O valor do item ou da parcela na condição {descricao} é de R$ {preco:.2f}, a ser pago em {qtd_parcelas} parcelas.')

