pessoas = soma = 0
lista_dados = []
mulheres = []




while True:
    dados = {}
    dados['nome'] = str(input('nome: '))
    dados['sexo'] = str(input('sexo (M/F): '))
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('idade: '))
    soma += dados['idade']
    pessoas += 1
    lista_dados.append(dados.copy())
    sair = str(input("quer continuar (s/n): "))
    while sair not in ('Ss,Nn'):
         sair = str(input("erro, só aceitamos (s/n): "))    
    if sair in 'Nn':
        break



media = soma / pessoas

acima_da_media = []
for pessoa in lista_dados:
    if pessoa['idade'] > media:
        acima_da_media.append(pessoa)



print('-='*30)
print(f'A) o grupo tem {pessoas} pessoas')
print(f'B) a media de idade é de {media:.2f}')
print(f'C) as mulheres cadastradas foram: ', end='')
for v in range(0, len(mulheres)):
    print(f'{mulheres[v]} ' , end='')
print(f'\nD) a lista de pessoas que estão acima da média são: ')
for p in acima_da_media:
    print(f"    Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}")