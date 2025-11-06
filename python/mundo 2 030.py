somah = 0
mais18 = 0
mulher20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = ''
    while sexo not in ['M', 'F']:
           sexo = input("Informe seu sexo (M/F): ").strip().upper()[0]
    if      sexo == 'M':
          somah += 1
    if  sexo == 'F' and idade < 20:
       mulher20 += 1

    cont = ''
    while cont not in ['S', 'N']:
        cont = input("Deseja continuar? (S/N): ").strip().upper()[0]
       

    if cont == 'N':
        break

print (f'o total de pessoas com mais de 17 é de {mais18}')
print(f'a quantidade de homens é de {somah}')
print(f'a quantidade de mulheres com menos de 20 anos é de {mulher20}')
   
   
   
   
   
    