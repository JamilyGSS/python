s = float(input('Digite seu salário: '))
if s <= 1250:
    a = (115 * s)/100
    print('O aumento será de 15% e o novo salário será de R${:.2f}'.format(a))
else:
    a = (110 * s)/100
    print('O aumento será de 10% e o novo salário será de R${:.2f}'.format(a))