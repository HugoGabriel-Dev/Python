# Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

# Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

numero_cpf = input('Informe o seu CPF ex:(000.000.000-00): ')
try:
    if not numero_cpf.isdigit():
        print('Erro: O CPF deve conter apenas números.')
    elif len(numero_cpf) != 11:
        print('Erro: O CPF deve ter exatamente 11 dígitos.')
    else:
        cpf = int(numero_cpf)
        print(f'CPF {cpf} recebido com sucesso!')
except:
    print('ERRO INESPERADO')