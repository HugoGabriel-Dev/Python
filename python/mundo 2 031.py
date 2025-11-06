soma = 0
maisdemil = 0
barato = 0
quant = 0
nomebarato = ''
while True:
    nome = str(input("NOME DO PRODUTO: "))

    
    preço = float(input('PREÇO DO PRODUTO: '))
    soma += preço
    quant+=1
    if quant == 1:
        barato = preço
        nomebarato = nome 
    else:
            if preço < barato:
                             barato = preço
                             nomebarato = nome
        
    
    if preço >= 1000:
             maisdemil += 1
   
    cont =' '
    while cont not in ['S', 'N']:
            cont = input("Deseja continuar? (S/N): ").strip().upper()[0]



    if cont == 'N':
        break 
print(f'o total de compras foi R${soma}')
print(f'temos {maisdemil} produto(s) custando mais de R$1000.00')
print(f'o produto mais barato foi {nomebarato} custando R${barato}')