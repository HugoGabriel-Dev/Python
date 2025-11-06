from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1' : randint(0, 6),
        'jogador2' : randint(0, 6),
        'jogador3' : randint(0, 6),
        'jogador4' : randint(0, 6)
}
ranking = []
print('VALORES SORTEADOS: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
print('-='*30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)