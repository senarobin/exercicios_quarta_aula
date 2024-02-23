
palavra = input('Escreva um nome: ')

palavra_reverso = palavra[::-1]


if palavra == palavra_reverso:
    print('no nome é um palíndromo')
else: 
    print('Não é um palíndromo')