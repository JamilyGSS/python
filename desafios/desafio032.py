ano = int(input('Digite o ano: '))
if ano % 4 != 0:
    print(ano, ' não é um ano bissexto.')
else:
    if ano % 100==0 and ano % 400 != 0 :
        print(ano, ' não é um ano bissexto.')
    else:
        print(ano, 'é bissexto!')
