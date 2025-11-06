year = 2025
contmaior = 0
contmenor = 0

for i in range(1, 8):
    ano = int(input(f"EM QUE ANO A {i} PESSOA NASCEU? "))
    idade = 2025 - ano
    if idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
        
print (f"ao todo tivemos {contmaior} maioresm de idade ")
print (f'ao todo tivemos {contmenor} menores de idade ')