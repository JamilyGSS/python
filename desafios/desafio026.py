frase = input('Frase: ').strip()
print('Quantidade de vezes que a letra A aparece: {}'.format(frase.upper().count('A')))
print('Posição em que A aparece pela primeira vez: {}'.format(frase.upper().find('A')+1))
print('Posição em que A aparece pela última vez: {}'.format(frase.upper().rfind('A')+1))
