from random import randint
from time import sleep

print('-' * 30)
print('     JOGO DA MEGA SENA     ')
print('-' * 30)

lista = []
jogos = []
perg = int(input('Quantos jogos você quer sortear? '))
total = 1

while total <= perg:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-' * 30)
print('JOGOS GERADOS:')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)

print('-' * 30)
print('BOA SORTE!')
