num1 = int(input("digite um numero: "))
contador = 0
for i in range (1 ,num1 + 1):
    if num1 % i == 0:
       print(f'\033[34m{i}\033[m', end = ' ')
       contador += 1 # Azul para divisores
    else:
        print(f'\033[33m{i}\033[m', end = ' ') 
print (f'\no numero {num1} foi divisivel {contador} vezes ')
if contador == 2:
    print ('portanto ele é primo ')
else :
    print ('portanto ele não é primo ')
    
        
        
