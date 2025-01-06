#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = float(input('Informe o primeiro número '))
num2 = float(input('Informe o segundo número '))
num3 = float(input('Informe o terceiro número '))

#Definindo o menor e o maior número
menor = num1
if num2 < num1 and num3 < num2:
    menor = num1
if num3 < num1 and num3 < num2:
    menor = num3

if num1 > num2 and num1 > num3:
    maior = num1
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O número {menor} é o menor, e o número {maior} é o maior.')

