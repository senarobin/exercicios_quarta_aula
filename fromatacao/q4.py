nome = input('Digite seu nome completo: ')

primeira_letra = nome[0]

pos = nome.index(' ') + 1 
segunda_letra = nome[pos]

pos = nome.index(' ', pos) + 1
terceira_letra = nome[pos]

pos = nome.index(' ', pos) + 1
quarta_letra = nome[pos]

pos = nome.index(' ', pos) + 1
quinta_letra = nome[pos]

sigla = primeira_letra + segunda_letra + terceira_letra

print(sigla)