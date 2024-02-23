import re

frase = 'Computador desligado'

substituir = re.sub(r'\*:\S+', 'aeiou', '*', frase)

print(substituir)
