produtos = (
    'Arroz', 56.99,
    'Feijão', 7.49,
    'Macarrão', 3.89,
    'Óleo', 60.79,
    'Açúcar', 4.29,
    'Café', 102.90,
    'Leite', 4.99,
    'Farinha', 3.49,
    'Biscoito', 22.79,
    'Refrigerante', 6.50
)
print('-=-' * 14)
print(f'{'lista de compras':^40}')
print('-=-' * 14)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<32}',end ='')
    else:
        print(f'R$ {produtos[pos]:>6.2f}')
print('-=-' * 14)



