dias = int(input('Qualtos dias alugados? '))
km = float(input('Quantos km rodados? '))
diaria = dias*60
kmrodado = km*0.15
total = diaria + kmrodado
print('O total a pagar é de R${:.2f}'.format(total))