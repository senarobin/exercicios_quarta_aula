hora_aleatoria = input('Digite uma hora aleatória. E:. 18:30:55: ')

horas, minutos, segundos = map(int, hora_aleatoria.split(':'))

total_segundos = horas * 3600 + minutos * 60 + segundos

print(f"Essa hora transformada em segundos é {total_segundos}")