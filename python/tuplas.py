# nomes = ( 
#     'joao', 7.5,
#     'maria', 8.0,
#     'hugo', 9.5,
#     'marcos', 6.0
# )

# for pos in range(0, len(nomes)):
#     if pos % 2 == 0:
#         print(f'{nomes[pos]} - ', end='')
#     else:
#         print(f'{nomes[pos]}')

# from random import randint

# numeros = tuple(randint(1, 100) for _ in range(10))
# print('Números:', numeros)
# print('Maior:', max(numeros))
# print('Menor:', min(numeros))

# numeros_extenso = (
#     'zero', 'um', 'dois', 'três', 'quatro',
#     'cinco', 'seis', 'sete', 'oito', 'nove',
#     'dez', 'onze', 'doze', 'treze', 'quatorze',
#     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
#     'vinte'
# )
# while True:
#     num = int(input("digite um numero "))
#     if 0 <= num <= 20:
#         print(f'{numeros_extenso[num]}')
#         break
#     else:
#         print(f'digite um valor valido ')

# nomes = (
#     'Lucas', 'Mariana', 'João', 'Carla', 'Pedro',
#     'Ana', 'Gustavo', 'Fernanda', 'Rafael', 'Jéssica',
#     'Bruno', 'Larissa', 'Diego', 'Camila', 'Igor',
#     'Bianca', 'Vinícius', 'Patrícia', 'Thiago', 'Isabela'
# )
# for i in nomes:
#     print(f'\nna palavra {i} tem: ',end='')
#     for letra in i:
#         if letra in 'aeiou':
#             print (f'{letra}', end =' ')


# num = (
#     int(input('Digite um número: ')),
#     int(input('Digite um número: ')),
#     int(input('Digite um número: ')),
#     int(input('Digite um número: '))
# )

# print(f'\nVocê digitou: {num}')
# print(f'O número 9 apareceu {num.count(9)} vez(es)')

# # Verifica se o número 3 está na tupla antes de tentar encontrar a posição
# if 3 in num:
#     print(f'O valor 3 apareceu na posição {num.index(3)+1}ª')
# else:
#     print('O valor 3 não foi digitado')

# # Mostra apenas os números pares
# print('Números pares digitados:', end=' ')
# for n in num:
#     if n % 2 == 0:
#         print(n, end=' ')


# produtos = (
#     'Arroz', 56.99,
#     'Feijão', 7.49,
#     'Macarrão', 3.89,
#     'Óleo', 60.79,
#     'Açúcar', 4.29,
#     'Café', 102.90,
#     'Leite', 4.99,
#     'Farinha', 3.49,
#     'Biscoito', 22.79,
#     'Refrigerante', 6.50
# )

# print('-=' *30)
# print(f'{'lista de produtos':^55}')
# print('-=' *30)
# for pos in range(0, len(produtos)):
#     if pos % 2 == 0:
#         print(f'{produtos[pos]:.<32}', end='')
#     else:
#         print(f'R$ {produtos[pos]:>6.2f}')  




# valores = []
# for v in range(0, 5):
#     n = int(input(f'Digite o valor para posição {v}: '))
#     valores.append(n)
#     if v == 0:
#         maior = menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n

# print('-='*30)
# print(f'Você digitou os valores: {valores}')
# print(f'O maior valor foi {maior} nas posições ', end='')
# for i, valor in enumerate(valores):
#     if valor == maior:
#         print(f'{i}... ', end='')

# print(f'\nO menor valor foi {menor} nas posições ', end='')
# for i, valor in enumerate(valores):
#     if valor == menor:
#         print(f'{i}... ', end='')


valores = []


while True:
        n = int(input("digite um valor: "))
        valores.append(n)

        sair = str(input(' quer continuar (S/N): ')).lower().strip()


        while sair not in ['s', 'n']:

            print('respota errada!, apenas (S/N) ')
            sair = str(input(' quer continuar (S/N): ')).lower().strip()


        if sair in ['s', 'n']:      

            if sair == 's':
                continue
        

            elif sair == 'n':
                break
        
        else:
                print('valor não correspondente')

b = []
c = []


for p in range(0, len(valores)):
     if p % 2 ==0:
       b.append(valores[p]) 
     else :
          c.append(valores[p])

print(f'lista completa: {valores}')
print(f'a lista de pares: {b}')
print(f'a lista de impares: {c}')