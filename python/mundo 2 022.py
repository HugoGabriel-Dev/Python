import time

pv = int(input("digite o primeiro valor: "))
sv =  int(input("digite o segundo valor: "))
sair = False
while not sair:
    print ("[1] somar ")
    print ("[2] multiplicar ")
    print ("[3] maior ")
    print ("[4] novos números ")
    print ("[5] sair do programa ")
    opcao = int(input('escolha uma opção: '))
    if opcao == 1:
        print (f'a soma entre {pv} e {sv} é {pv + sv}')
        print("=-" * 20)
        print(time.sleep(1))
    elif opcao == 2:
        print(f"a multiplicação entre {pv} x {sv} é {pv * sv}")
        print("=-" * 20)
        print(time.sleep(1))
    elif opcao == 3:
        if pv > sv:
            print(f'{pv} é maior que {sv}')
            print("=-" * 20)
            print(time.sleep(1))
        else :
            print(f'{sv} é maior que {pv}')
            print("=-" * 20)
            print(time.sleep(1))
    elif opcao == 4:
        pv = int(input('novo valor: '))
        sv = int(input('novo valor: '))
        print("=-" * 20)
        print(time.sleep(1))
    elif opcao == 5:
        sair = True
        print("=-" * 20)
        print(time.sleep(1))
        print('programa encerrado!, até logo!(: ')
    else:
        print('tente novamente! ')
        print("=-" * 20)
        print(time.sleep(1))