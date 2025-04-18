n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
else:
    if n2 < menor:
        menor = n2

if n3 > maior:
    maior = n3
else:
    if n3 < menor:
        menor = n3

print('Menor número: ', menor)
print('Maior número: ', maior)