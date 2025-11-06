nomes = (
    'Lucas', 'Mariana', 'João', 'Carla', 'Pedro',
    'Ana', 'Gustavo', 'Fernanda', 'Rafael', 'Jéssica',
    'Bruno', 'Larissa', 'Diego', 'Camila', 'Igor',
    'Bianca', 'Vinícius', 'Patrícia', 'Thiago', 'Isabela'
)

for i in nomes:
    print(f'\nna palavra {i} temos : ', end='')
    for letra in i:
        if letra in 'aeiou':
            print(f'{letra}', end = ' ')