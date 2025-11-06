def leiInt (msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('por favor, digite um numero inteiro valido! ') 
            continue
        except(KeyboardInterrupt):
            print('\nusuario preferiu não digitar um numero! ')
            return 0
        else:
            return n
        
num = leiInt('digite um numero inteiro: ')
print(f'o numero que voce digitou foi {num}')