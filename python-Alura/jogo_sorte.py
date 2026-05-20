# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

import random

opcoes = ['pedra', 'papel', 'tesoura']

opcao_maquina = random.choice(opcoes)
opcao_jogador = input('Qual será sua jogada(pedra, papel ou tesoura)? ')
opcao_jogador_formatada = opcao_jogador.lower()

if opcao_jogador_formatada in opcoes:
    if opcao_jogador_formatada == opcao_maquina:
        print(f'A maquina escolheu: {opcao_maquina}')
        print(f'Você escolheu: {opcao_jogador_formatada}')
        print('Empate!!!')
    elif (opcao_jogador_formatada == 'pedra' and opcao_maquina == 'tesoura') or \
         (opcao_jogador_formatada == 'papel' and opcao_maquina == 'pedra') or \
         (opcao_jogador_formatada == 'tesoura' and opcao_maquina == 'papel'):
        print(f'A maquina escolheu: {opcao_maquina}')
        print(f'Você escolheu: {opcao_jogador_formatada}')
        print('Você ganhou!')
    else:
        print(f'A maquina escolheu: {opcao_maquina}')
        print(f'Você escolheu: {opcao_jogador_formatada}')
        print('Você perdeu!')
else:
    print('ERRO, OPÇÃO INVÁLIDA!')
