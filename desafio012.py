"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""
preco=float(input('Informe o preço do item: R$ '))
preco_com_desconto=preco-(preco*0.05)
print('O preço original do produto é R$ {:.2f} . Seu preço com o desconto é de R$ {:.2f} .'.format(preco, preco_com_desconto))