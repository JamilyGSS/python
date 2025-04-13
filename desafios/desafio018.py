from math import cos, sin, tan, radians
a = float(input('Digite o valor do ângulo: '))
rad = radians(a)
print('seno de {} : {:.2f} \n cosseno de {}: {:.2f} \n tangente de {} : {:.2f}'.format(a, sin(rad), a, cos(rad), a, tan(rad)))