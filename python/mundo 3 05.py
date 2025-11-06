from random import randint
from time import sleep


def escolha (lista):
    print(f'sorteando 5 valores da lista: ', end='')
    for cont in range (0, 5):
       n = randint(1, 10)
       lista.append(n)
       print(f'{n}', end=' ', flush=True)
       sleep(0.5)

def somapar (lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\na soma dos valores pares é {soma}')









numeros = list()
escolha(numeros)
somapar(numeros)
