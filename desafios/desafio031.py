d = float(input('Qual a distância da viagem em km? '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('O preço da passagem é de R${:.2f}'.format(p))