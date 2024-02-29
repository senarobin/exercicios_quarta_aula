
palavra = input('Escreva uma palavra: ')

palavra_reverso = palavra[::-1]


if palavra == palavra_reverso:
    print('É um palíndromo')
else: 
    print('Não é um palíndromo')