dados = {}
gols = []
tot = 0
dados['nome'] = str(input('nome do jogador: '))
partidas = int(input(f'quantas partidas {dados["nome"]} jogou: '))
for p in range(1, partidas+1):
    go = ( int(input(f'quantos gols na partida {p}? ')))
    gols.append(go)
    tot += go
dados['gols'] = gols
dados['total'] = tot
print('-='*30)
print(dados)
print('-='*30)
print(f'o campo nome tem valor {dados["nome"]} ')
print(f'o campo gols tem valor {dados["gols"]} ')
print(f'o campo total tem valor {dados["total"]} ')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas. ')
for i, v in enumerate(gols):
    print(f'      => NA PARTIDA {i+1}, FEZ {v}     ')
print(f'fez o total de {dados["total"]} gols ')