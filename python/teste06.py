# append --> adicionar um termo a lista ultimo
# insert --> inserir em uma posição especifica 
# del --> exclui pelo indice algo da lista []
# pop --> exclui pelo indice tambem(normalmente o ultimo) ()
# remove --> exclui pelo nome que esta na lista 
# sort --> deixa os valores ordenados de forma crescente
# sort(resverse=True) --> organiza os valores e coloca-os de forma decrescente
# enumerate --> mostra o indice e valores da variavel composta



valores = []
maior = 0
menor = 0
for v in range(0, 5):
    n = (int(input(f'Digite o valor para posição {v}: ')))
    valores.append(n)
    if v == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('-='*30)
print(f'você digitou os valores {valores}')
print(f'o maior valor foi {maior} nas posições ' , end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f' {i}...' ,end='')


print(f'\no menor valor foi {menor} nas posições' ,end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f' {i}...' ,end='')
