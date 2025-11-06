jogadores = []

while True:
    dados = {}
    gols = []
    tot = 0
    dados['nome'] = str(input('nome do jogador: '))
    partidas = int(input(f'quantas partidas {dados["nome"]} jogou: '))

    for p in range(1, partidas+1):
        go = ( int(input(f'quantos gols na partida {p}? ')))
        gols.append(go)
        tot += go

    dados['gols']= gols[:]
    dados['total']= tot
    jogadores.append(dados.copy())


    sair = str(input('quer continuar (s/n): ')).strip().lower()
    while sair not in ('s', 'n'):
         sair = str(input('erro, apenas (s/n): ')).strip().lower()

    if sair == 'n':
            break
    
print('-='*30)
print(f'{"cod":<3} {"nome":<10}{"gols":<15}{"total"}')
print('-='*30)
for i, v in enumerate(jogadores):
    print(f'  {i:<2}{v["nome"]:<10}{str(v["gols"]):<15}{v["total"]}')
print('--'*30)
while True:
     resp = int(input('qual jogador você deseja ver as estatisticas? (999 interrompe)'))
     if resp == 999:
        print('FINALIZANDO PROGRAMA!')
        break
     if 0 <= resp < len(jogadores) :
          print(f'-- LEVANTANDO DADOS DO JOGADOR {jogadores[resp]['nome']}')
          for i, v in enumerate(jogadores[resp]['gols']):
               print(f'    No jogo {i+1} fez {v} gols')

          
          
          
