# def fatorial (n, show=False):
#     """_summary_

#     Args:
#         n (_type_): _description_
#         show (bool, optional): _description_. Defaults to False.

#     Returns:
#         _type_: _description_
#     """
#     f = 1
#     for i in range(n, 0, -1):
#         if show:
#             print(f'{i}', end='')
#             if i > 1:
#                 print(f' x ' ,end='')
#             else:
#                 print(f' = ', end='')
#         f *= i
#     return f
# print(fatorial(5))    



def fatorial (n, show=False):
    f = 1 
    for i in range(n, 0, -1):
        if show == True:
            print(f'{i}', end='')
            if i > 1:
                print(f' {'x'} ', end='')
            else:
                print(f'{'='} ', end='')
        f *= i
    return f

while True:
    num = int(input('digite um numero: '))
    print(fatorial(num))
    calc = str(input('deseja ver o calculo (s/n): '))
    if calc in 'sS':
        print(fatorial(num, show=True))
    else:
        print('ok, obrigado pela atenção! ')
    sair = str(input("deseja continuar? (s/n): "))
    if sair in 'nN':
        break
    
        