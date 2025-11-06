valores = []

for i in range(5):
    n = int(input('Digite um número: '))
    if i == 0 or n > valores[-1]:  # Se for o primeiro ou maior que o último
        valores.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {valores}')
