email = input('Digite seu e-mail: ')

nome_usuario = email.split('@')[0]
nome_dominio = email.split('@')[1]

print(nome_usuario)
print(nome_dominio)
'''
pos = nome.index(' ') + 1 
segunda_letra = nome[pos]'''