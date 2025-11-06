def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.strip().lstrip('-').isdigit():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')

