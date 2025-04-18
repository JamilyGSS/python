num = int(input('Digite um número: '))
print('O dobro de {} é \033[4;31;107m{}\033[m, o triplo de {} é \033[4;31;107m{}\033[m e a raiz quadrada de {} é \033[4;31;107m{:.2f}\033[m'.format(num,2*num,num,3*num,num,num**(1/2)))
