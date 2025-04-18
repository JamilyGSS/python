m = int(input('Digite a medida em metros: '))
cm = m*100
mm = m*1000
print('\033[4;31m{}\033[m metros é igual à \033[4;32m{}\033[m cm e à \033[4;34m{}\033[m mm.'.format(m,cm,mm))