

maior = 0
menor = 0

for i in range(1, 8):
    peso = float(input(f'Digite o peso da pessoa {i}: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"\nO maior peso lido foi {maior} kg")
print(f"O menor peso lido foi {menor} kg")



