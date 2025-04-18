import random
nc = random.randint(0,5)
print('-=-' * 20)
nu = int(input('Tente descobrir o número inteiro entre 0 e 5 pensado pelo computador: '))
print('-=-' * 20)
if nu == nc:
    print('Parabéns, você acertou!')
else:
    print('Você errou! O número escolhido pelo computador foi', nc)