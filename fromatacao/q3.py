import re

frase = input('Digite uma frase: ')

substituir = re.sub('[aeiou]', '*', frase)

print(f'A frase vai ficar {substituir}')
