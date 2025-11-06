from time import sleep

def contador (i, f, p):
     if p == 0:
        p = 1
     if p < 0:
        p = -p
     print(f'\ncontagem de {i} ate {f} de {p} em {p}')
     if i < f:
        cont = i
        while cont <= f:
            print(F'{cont}', end=' ', flush=True)
            sleep(0.5)
            i += p
            cont += p
     else:
     
         cont = i
         while cont >= f:
             print(f'{cont}', end=' ', flush=True)
             sleep(0.5)
             cont -= p


contador (1, 10, 1)
contador(10, 0, 2)

print('\nsua vez de personalizar. digite sua contagem: ')
ini = int(input('INICIO:  '))
fim = int(input('FIM:     '))
passo = int(input('PASSO: '))
contador (ini, fim, passo)