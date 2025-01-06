"""
Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "A"
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez
"""
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase, aparecendo primeiro na posição {} e por último na posição {}'.format(frase.count('A'),frase.find('A'),frase.rfind('A')))
