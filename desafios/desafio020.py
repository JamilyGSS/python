import random
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
alunos = [a1,a2,a3,a4]
sorteado = random.choice(alunos)
print(f'O aluno escolhido foi: {sorteado}')
random.shuffle(alunos)
print('A ordem de apresentação será')
print(alunos)