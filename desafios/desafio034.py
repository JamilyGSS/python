s = float(input('Digite seu salário: '))
if s <= 1250:
    a = (115 * s)/100
else:
    a = (110 * s)/100
print('O salário antigo R${:.2f} será aumentado para R${:.2f}'.format(s,a))