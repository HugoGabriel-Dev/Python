# Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

# Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
import os

def menu():
    print('1. Adicionar tarefa ')
    print('2. visualizar tarefas ')
    print('3. remover tarefa ')
    print('4. sair ')
def sair():
    print('Programa finalizado, volte sempre!')


tarefas = []
while(True):
    os.system('cls')
    menu()
    opcao_escolhida = int(input('Digite a Opção desejada: '))
    if opcao_escolhida in [1, 2, 3, 4]:
        if opcao_escolhida == 1:
            os.system('cls')
            nova_tarefa = input('Digite qual tarefa você deseja adicionar: ')
            tarefa_formatada = nova_tarefa.lower()
            tarefas.append(tarefa_formatada)
            print('\nTarefa adicionada com sucesso!\n')
            input('clique em qualquer tecla para voltar ao menu: ')
            continue
        elif opcao_escolhida == 2:
            os.system('cls')
            print('Menu de tarefas: ')
            for tarefa in tarefas:
                print(f'| {tarefa} |')
            input('clique em qualquer tecla para voltar ao menu: ')
            continue
        elif opcao_escolhida == 3:
            os.system('cls')
            nome_tarefa_remover = input('Digite o nome da tarefa que deseja remover: ')
            tarefa_remover = nome_tarefa_remover.lower()
            if tarefa_remover in tarefas:
                tarefas.remove(tarefa_remover)
                print(f'Tarefa {tarefa_remover} removida com sucesso!!!\n')
                input('clique em qualquer tecla para voltar ao menu: ')
                continue
            else:
                print('Tarefa não encontrada na lista de tarefas! \n')
                input('clique em qualquer tecla para voltar ao menu: ')
                continue
        else:
            sair()
            break
    else:
        continue