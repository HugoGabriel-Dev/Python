valor = int(input("qual o valor da casa? "))
salario = float(input("qual o seu salario? "))
tempo = int(input('qual o tempo do imprestimo em anos? '))

ano = tempo * 12
porctmin = (salario * 30) / 100
prestação = valor / ano 

if prestação <= porctmin :
    print(f'para pegar uma casa de {valor} em {tempo} anos a prestação será de {prestação:.2f}')
    print("ACESSO PERMITIDO!")
else: 
    print(f'para pegar uma casa de {valor} em {tempo} anos a prestação será de {prestação:.2f}')
    print('ACESSO NEGADO!')


