import random
nc = random.randint(0,5)
nu = int(input('Tente descobrir o número inteiro entre 0 e 5 pensado pelo computador: '))
if nu == nc:
    print('Parabéns, você acertou!')
else:
    print('Você errou! O número escolhido pelo computador foi', nc)