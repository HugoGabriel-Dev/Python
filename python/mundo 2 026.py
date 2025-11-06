cont = 0 
soma = 0
maior = 0
menor = 0

while True:
          num = int(input('digie um numero: ')) 
          cont += 1
          soma += num   
          if cont == 1:
               maior = num
               menor = num
          else:
               if num > maior:
                    maior = num
               elif num < menor:
                    menor = num          
          while True:
               sair = str(input("quer continuar? (s/n): ")).lower().strip()[0]
               
               if sair == 's':
                    break  # sai do loop interno e continua o loop principal
               elif sair == 'n':
                     print(f'\nTotal de números digitados: {cont}')
                     print(f'Soma total: {soma}')
                     print(f'Média: {soma / cont:.2f}')
                     print(f'Maior número: {maior}')
                     print(f'Menor número: {menor}')
                     exit()
               else:
                    print('Opção inválida, digite "s" ou "n".')

 

