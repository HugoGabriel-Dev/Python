from random import randint
maior = 0
menor = 0
numeros = (randint (1, 10),randint (1, 10),randint (1, 10),randint (1, 10),randint (1, 10))




for n in numeros:
    print(n, end = ' ')


    
print(f'\no maior foi {max(numeros)}')
print(f'o menor foi {min(numeros)}')