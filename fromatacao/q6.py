"""frase = input('Digite uma frase: ')"""
frase = '''Resposta verificada por especialistas. Uma pessoa aleatória é uma pessoa qualquer em determinado contexto.
 O vocábulo "aleatório" diz respeito a algo que está solto ao acaso e que não é algo determinado.
Logo, uma pessoa aleatório pode ser considerada uma pessoa que não está determinada, qualquer uma'''

quant_caracteres = frase.replace(' ', '')
quant_caracteres = len(quant_caracteres)
quant_palavras = len(frase.split())
quant_linhas = len(frase.splitlines())


print(f"A quantidade de caracteres é {quant_caracteres}, de palavras é {quant_palavras} e de linhas é {quant_linhas}")