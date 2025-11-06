somaidade = 0
meidaidade = 0
maioridademaisvelho = 0
nomemaisvelho = ''
totmulher20 = 0

for i in range (1, 5):
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input("sexo M/F: ")).strip().upper()
    somaidade += idade
    
    if sexo == 'M':
        if idade > maioridademaisvelho:
            maioridademaisvelho = idade
            nomemaisvelho = nome
        if sexo == 'F' and idade > 20:
            totmulher20 += 1
            
meidaidade = somaidade / 4
print(f'a idade media do grupo é de: {meidaidade}')
print(f'o homem mais velho tem {maioridademaisvelho} anos e se chama {nomemaisvelho}')
print(f'a quantidade de {totmulher20} mulheres com mais de 20 anos ')
