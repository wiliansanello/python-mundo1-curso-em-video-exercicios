valor = int(input('Digite um valor de 0 a 9999: '))
print('Unidade: {}'.format((valor // 1) % 10 ))
print('Dezena: {}'.format((valor // 10) % 10))
print('Centena: {}'.format((valor // 100) % 10))
print('Milhar: {}'.format((valor // 1000 % 10)))