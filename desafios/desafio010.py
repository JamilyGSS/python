real = float(input('Digite o valor em reais: '))
dolar = real/3.27
print('Com \033[1;32mR${}\033[m você pode comprar \033[1;34mUS${:.2f}'.format(real,dolar))