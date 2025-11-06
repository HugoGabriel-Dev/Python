num = ( int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')))

print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('não tem nenhum 3 no grupo de numeros')
for n in num :
    if n % 2 == 0:
     print(f'os valores pares foram {n}')

        
