valores = []
b = []
c = []

while True:
        n = int(input("digite um valor: "))
        valores.append(n)
        if n % 2 ==0 :
            b.append(n)
        else:
             c.append(n)

        sair = str(input(' quer continuar (S/N): ')).lower().strip()


        while sair not in ['s', 'n']:

            print('respota errada!, apenas (S/N) ')
            sair = str(input(' quer continuar (S/N): ')).lower().strip()


        if sair in ['s', 'n']:      

            if sair == 's':
                continue
        

            elif sair == 'n':
                break
        
        else:
                print('valor não correspondente')

print(f'lista completa: {valores}')
print(f'a lista de pares: {b}')
print(f'a lista de impares: {c}')