soma = 0
contador = 0

for p in range (1, 7):
    numero = int(input("digite um numero "))
    if numero % 2 == 0:
         soma = soma + numero
         contador = contador + 1
print(f'a soma dos valores pares são : {soma}, foram {contador} somados')