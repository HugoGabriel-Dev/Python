# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

import random

while True:
    # Já colocamos o .lower() direto aqui para limpar a entrada na hora!
    escolha_jogador = input('Escolha qual será sua jogada (pedra, papel ou tesoura): ').lower()
    
    # Criamos uma lista com as opções válidas
    opcoes_validas = ['pedra', 'papel', 'tesoura']
    
    # Usamos o operador 'in' para checar se a resposta está na lista
    if escolha_jogador in opcoes_validas:
        escolha_computador = random.choice(opcoes_validas)
        print(f'MINHA JOGADA FOI {escolha_computador}')
        if escolha_jogador == escolha_computador:
            print('Resultado: Deu Empate! 🤝')
            break

        elif(escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
            (escolha_jogador == 'tesoura' and escolha_computador == 'papel') or \
            (escolha_jogador == 'papel' and escolha_computador == 'pedra'):
            print('Resultado: Você Venceu! 🎉 Parabéns!')
            break
            
        else:
            print('Resultado: O Computador Venceu! 🤖')
            break # Sai do loop e continua o jogo
    else:
        print("Opção inválida! Tente novamente.")
        # Não precisa do segundo input aqui embaixo, o while True já vai voltar para o começo!

