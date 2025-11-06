# append --> adicionar um termo a lista ultimo
# insert --> inserir em uma posição especifica 
# del --> exclui pelo indice algo da lista []
# pop --> exclui pelo indice tambem(normalmente o ultimo) ()
# remove --> exclui pelo nome que esta na lista 
# sort --> deixa os valores ordenados de forma crescente
# sort(resverse=True) --> organiza os valores e coloca-os de forma decrescente
# enumerate --> mostra o indice e valores da variavel composta
# clear --> apaga os dados de uma variavel( seja ela composta ou não )





# galera = []
# dados = []
# maior = menor = 0
# for i in range(3):
#     dados.append(str(input('nome: ')))
#     dados.append(int(input('idade: ')))
#     galera.append(dados[:])
#     dados.clear()
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade')
#         maior += 1
#     else:
#         menor += 1
# print(f'{maior} maiores de idade e {menor} menores de idade') 



galera = []
dados = []
pessoas = 0
maior = menor = 0
while True:
    dados.append(str(input('nome: ')))
    dados.append(float(input('peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    resp = str(input('deseja continuar(s/n): '))
    if resp in 'nN':
        break 






print(f'{maior}')

