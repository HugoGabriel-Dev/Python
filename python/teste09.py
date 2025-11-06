elementos = 0
valores = []
while True:
        n = int(input("digite um valor: "))
        elementos += 1
        valores.append(n)
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

valores.sort(reverse=True)

print(f'você digitou {elementos} elementos')
print(f'os valores em ordem decrescente são {valores}')
if 5 in valores:
     print(f'o valor 5 faz parte da lista ')
else:
     print(f'o valor 5 não faz parte da lista ')