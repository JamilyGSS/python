# print('\033[97molá mundo\033[m')

# a = 2
# b = 3
# print('Os valores são \033[4;31m{}\033[m e \033[1;97;40m{}\033[m'.format(a,b))

# nome = 'Gustavo'
# print('Olá! Prazer em te conhecer, {}{}{}'.format('\033[4;97m',nome,'\033[m'))

nome = 'Gustavo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;97m'}
print('Olá! Prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))