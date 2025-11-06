primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10  # Começa mostrando 10 termos

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos você quer mostrar? '))

print('FIM')
