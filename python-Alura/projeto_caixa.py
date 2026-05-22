# Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

# Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

# import os
# import time

# cedulas_caixa = [100, 50, 20, 10, 5, 2]
# contador_cedulas = [0, 0, 0, 0, 0, 0]

# while(True):
#     valor_saque = input('Digite o valor que deseja sacar: ')
#     try:
#         valor_saque = int(valor_saque)
#         novo_valor = valor_saque
#         if novo_valor % 2 == 0:
#             print(f'Processando seu saque...')
#             time.sleep(3)
#             for i, v in enumerate(cedulas_caixa):
#                 if novo_valor > v:
#                     novo_valor -= v

#             break
#         else:
#             print('Erro: O valor deve ser múltiplo de 2.')
#             continue

#     except ValueError as erro:
#         print(f'Valor deve ser um número: {erro}')
#         continue


valor = [100, 20, 10]
out = 1035
for i, v in enumerate(valor):
    while(out > v):
        out -= v
print(out)
