soma = 0  # Acumulador da soma
contador = 0  # Contador de quantos números foram somados

for numero in range(1, 7):
    if numero % 2 == 0:
        soma += numero
        contador += 1

print(soma)
