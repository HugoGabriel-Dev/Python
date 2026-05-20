# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

import calculadora

calculadora.menu()

while True:
    opcao_usuario = input('Escolha qual operação você irá usar: ')

    try:
        opcao_usuario = int(opcao_usuario)
    except ValueError:
        print('Opção inválida!, Digite um número!!!')
        continue

    # Verificamos se a opção está entre as válidas (1 a 4) antes de pedir os números
    if opcao_usuario in [1, 2, 3, 4]:
        try:
            # Pedimos os números aqui dentro, protegidos contra letras (ValueError)
            primeiro_numero = float(input('Digite o primeiro número: '))
            segundo_numero = float(input('Digite o segundo número: '))
            
            # Colocamos o match dentro do try para capturar o ZeroDivisionError
            match opcao_usuario:
                case 1:
                    calculadora.somar(primeiro_numero, segundo_numero)
                    break
                case 2:
                    calculadora.subtrair(primeiro_numero, segundo_numero)
                    break
                case 3:
                    calculadora.mutiplicar(primeiro_numero, segundo_numero) # Cuidado com o erro de digitação 'mutplicar' lá na função!
                    break
                case 4:
                    calculadora.dividir(primeiro_numero, segundo_numero)
                    break
        except ValueError:
            print('Erro: Você digitou uma letra no lugar do número da conta!')
        except ZeroDivisionError:
            print('Erro: Não é possível dividir por zero!')
            
    else: # Seu caso default
        print('Opção inválida!!')
        continue