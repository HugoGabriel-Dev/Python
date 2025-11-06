def jogador (nome, v=0):
    print(f'o jogador {nome} fez {v} gols no campeonato! ')


# programa principal

n = str(input('NOME DO JOGADOR: ')).strip()
g = input('NUMEROS DE GOLS: ').strip()

if n == '':
    n = '<desconhecido>'
if g.isnumeric():
    g = int(g)
else:
    g = 0
jogador(n, g)



