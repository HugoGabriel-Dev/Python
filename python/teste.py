# times_brasileirao = (
#     'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians',
#     'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense',
#     'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras',
#     'Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória', 'Atlético-GO'
# )

# # Exibir os 5 primeiros colocados (posição 1 a 5)
# print("Top 5 do Brasileirão:")
# print('-=' * 20)
# print (f'times: {times_brasileirao}')
# print('-=' * 20)
# print (f'os cinco primeiros : {times_brasileirao[0:5]}')
# print('-=' * 20)
# print(f'os 4 ultimos : {times_brasileirao[-4:]}')
# print('-=' * 20)
# print(f'times em ordem alfabetica: {sorted(times_brasileirao)}')
# print('-=' * 20)
# print(f'o fluminense esta na {times_brasileirao.index("Fluminense")+1} posição ')

nomes = ("hugo gabriel ", 'ana', 'joao', 'ma')
for quant in range(len(nomes)):
    print(f'o nome {nomes[quant]} tem {len(nomes[quant])}')
