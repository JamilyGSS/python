v = float(input('Qual a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('VOCÊ ESTÁ MULTADO! A SUA MULTA SERÁ DE R${:.2f}'.format(m))