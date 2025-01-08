"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura**2)

print('Você está ', end = '')
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('no peso ideal')
elif imc >= 25 and imc < 30:
    print('com sobrepeso')
elif imc >= 30 and imc < 40:
    print('obeso')
else:
    print('com obesidade mórbida')