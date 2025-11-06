valores = []
while True:
    n = int(input("digite um valor: "))

    if n in valores:
        print('valor duplicado. não vou adicionar ')
    else:
        valores.append(n)
    sair = str(input(' quer continuar (S/N): ')).lower().strip()
    
    while sair not in ['s', 'n']:
        print('respota errada!, apenas (S/N) ')
        sair = str(input(' quer continuar (S/N): ')).lower().strip()
    
    
    if sair in ['s', 'n']:
        
        if sair == 's':
            continue
       

        elif sair == 'n':
            print('você saiu do programa ')
            break
    
    else:
        print('valor não correspondente')

print(sorted(valores))