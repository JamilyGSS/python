real = float(input('Digite o valor em reais: '))
dolar = real/3.27
print('Com R${} você pode comprar US${:.2f}'.format(real,dolar))