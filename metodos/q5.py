import re

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')

sep_palavras = frase.split()

palavra_muda = re.sub(sep_palavras, palavra)

print(palavra_muda)