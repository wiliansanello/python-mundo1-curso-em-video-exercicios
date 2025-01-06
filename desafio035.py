#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

lado1 = float(input('Informe o valor da primeira reta: '))
lado2 = float(input('Informe o valor da segunda reta: '))
lado3 = float(input('Informe o valor da terceira reta: '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print(f'Ótimo. As retas de valores {lado1}, {lado2} e {lado3} formam um triângulo')
else:
    print(f'Que pena. As retas de valores {lado1}, {lado2} e {lado3} não formam um triângulo')