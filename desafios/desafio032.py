from datetime import date
ano = int(input('Digite o ano: (Coloque 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year

if ano % 4 != 0 or ano % 100==0 and ano % 400 != 0:
    print(ano, 'não é um ano bissexto.')
else:
    print(ano, 'é bissexto!')
