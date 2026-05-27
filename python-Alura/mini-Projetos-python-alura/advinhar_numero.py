# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random


numero_escolhido_maquina = random.randint(1, 100)
while(True):
    opcao_jogador = input('Tente adivinhar o número (1-100): ')

    try:
        opcao_jogador = int(opcao_jogador)
        if opcao_jogador > 100 or opcao_jogador < 1:
            raise ValueError('Número fora do intervalo! Digite um número entre 1 e 100.')
        else:
            if opcao_jogador > numero_escolhido_maquina:
                print(f'Muito Alto, tente novamente: {opcao_jogador}')
            elif opcao_jogador < numero_escolhido_maquina:
                print(f'Muito Baixo, tente novamente: {opcao_jogador}')
            else:
                print(f'Você acertou, O número era: {numero_escolhido_maquina}')
                break
    except ValueError as erro:
        print(f'Entrada inválida: {erro}')