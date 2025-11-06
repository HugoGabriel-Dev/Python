dados = {}
ano = 2025
dados['nome'] = str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
dados['idade'] = ano - nascimento
dados['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if dados['ctps'] == 0:
    print('-='*30)
    print(f'nome: {dados["nome"]} ')
    print(f'idade: {dados["idade"]} ')
    print('não tem carteira de trabalho ainda ')
    exit()
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano da contratação: '))
    dados['salario'] = float(input('qual seu salario: R$'))
    ate = ((dados['contratação'] + 35) - ano) + dados['idade']
    dados['aposentadoria'] = ate
print('-='*30)
print(f'nome: {dados["nome"]} ')
print(f'idade: {dados["idade"]} ')
print(f'cpts: {dados["ctps"]} ')
print(f'contratação: {dados["contratação"]} ')
print(f'salário: {dados["salario"]} ')
print(f'aposentadoria: {dados["aposentadoria"]} ')
