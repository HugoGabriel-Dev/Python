sexo = ''
while sexo not in ['M','F']:
    sexo = str(input('digite seu sexo (F/M): ')).strip().upper()
if sexo == 'F':
    print (f"você é mulher")
else:
    print(f'você é homem!')