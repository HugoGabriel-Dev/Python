pares = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
coluna = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l] [c] = int(input(f'digite o valor para [{l}:{c}] '))
        if matriz[l] [c] % 2 == 0:
            pares += matriz[l] [c]
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'a soma dos pares é {pares}')
m = [matriz[0][2], matriz[1][2], matriz[2][2]]
soma_coluna3 = sum(m)
print(f'a soma da terceira coluna foi {soma_coluna3}')
s = [matriz[0][1], matriz[1][1], matriz[2][1]]
maior_coluna2 = max(s)
print(f'o maiopr valor da segunda coluna é {maior_coluna2}')
# for l in range(0, 3):
#     coluna += matriz[l][2]
# print(f'a soma da terceira coluna é {coluna}')
# for c in range(0, 3):
#     if c == 0:
#         maior = matriz[1][c]
#     elif matriz[1][c] > maior:
#         maior = matriz[1][c]
# print(f'o maior valor da segunda coluna é {maior}')
# Inicializa variáveis
# Inicializa variáveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0

# Entrada de dados e soma dos pares
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz[linha][coluna] = valor
        if valor % 2 == 0:
            soma_pares += valor

# Exibição da matriz formatada
print('\nMatriz digitada:')
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end=' ')
    print()

print('-=' * 30)

# Cálculos adicionais
soma_coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior_coluna2 = max([matriz[0][1], matriz[1][1], matriz[2][1]])

# Exibição dos resultados
print(f'➡️  Soma dos valores pares: {soma_pares}')
print(f'➡️  Soma dos valores da terceira coluna: {soma_coluna3}')
print(f'➡️  Maior valor da segunda coluna: {maior_coluna2}')
