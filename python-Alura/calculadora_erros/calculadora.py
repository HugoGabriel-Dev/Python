def somar(a = 0, b = 0):
    print(f'A soma de {a} + {b} = {a + b}')
def dividir(a = 1, b = 1):
    if b == 0:
        raise ZeroDivisionError
        exit()
    else:
        print(f'A divisão de {a} / {b} = {a / b}')
def mutiplicar(a = 0, b = 0):
    print(f'A multiplcação de {a} x {b} = {a * b}')
def subtrair(a = 0, b = 0):
    print(f'A subtração de {a} - {b} = {a - b}')

def menu():
    print('\n(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir\n')