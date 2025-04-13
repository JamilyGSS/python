import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
x = co**2 + ca**2
print('O valor da hipotenusa desse triângulo retângulo é {:.2f}'.format(math.sqrt(x)))