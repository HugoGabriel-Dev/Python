# Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

import os
import time

cedulas_caixa = [100, 50, 20, 10, 5, 2]

while(True):

    contador_cedulas = [0, 0, 0, 0, 0, 0]

    valor_saque = input('Digite o valor que deseja sacar: ')
    try:
        valor_saque = int(valor_saque)
        novo_valor = valor_saque

        if novo_valor <= 0:
            os.system('cls')
            print('Erro: O valor do saque deve ser maior que zero!')
            continue

        if novo_valor % 2 == 0:
            print(f'Processando seu saque...')

            for i, v in enumerate(cedulas_caixa):

                if v == 5:
                    continue

                while(novo_valor >= v):
                    novo_valor -= v
                    contador_cedulas[i] += 1

            time.sleep(3)
            os.system('cls')
            print('CÉDULAS ENTREGUES:\n')
            print(f'{contador_cedulas[0]} de R$100')
            print(f'{contador_cedulas[1]} de R$50')
            print(f'{contador_cedulas[2]} de R$20')
            print(f'{contador_cedulas[3]} de R$10')
            print(f'{contador_cedulas[4]} de R$5')
            print(f'{contador_cedulas[5]} de R$2')
            break
        else:
            os.system('cls')
            print('Erro: O valor deve ser múltiplo de 2.')
            continue
    except ValueError as erro:
        os.system('cls')
        print(f'Valor deve ser um número: {erro}')
        continue