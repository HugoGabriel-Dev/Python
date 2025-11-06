from random import randint

itens = ['pedra','papel','tesoura']
computador = randint (0,2)

print('''OPÇÕES: 
[0] pedra
[1] papel 
[2] tesoura
''')
jogador = int(input('qual sua jogada? '))
if jogador < 0 or jogador > 2:
    print('Jogada inválida!')
else:
    print(f'O computador jogou: {itens[computador]}')
    print(f'O jogador jogou: {itens[jogador]}')

if computador == jogador:
    print ('EMPATE')
elif (computador == 0 and jogador == 1) or \
     (computador == 1 and jogador == 2) or \
     (computador == 2 and jogador == 0):
    print(" JOGADOR VENCE! ")
else :
    print(" JOGADOR PERDE!")


