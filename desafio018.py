from math import sin, cos, tan, radians
ângulo = float(input('Informe o ângulo para definir os valores:'))
print('Para o ângulo {} graus, seu seno é {:.2f}, seu co-seno é {:.2f} e sua tangente é {:.2f}'
      .format(ângulo, sin(radians(ângulo)),cos(radians(ângulo)), tan(radians(ângulo))))