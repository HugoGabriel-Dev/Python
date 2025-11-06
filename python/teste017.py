# locadora = []
# filme = dict()
# filme = { 'nome':'star wars',
#         'ano': 1999,
#         'diretor':'george floyd'
# }
# filme['peso'] = 73.2
# filme['nome'] = 'hugo'

# for k, v in filme.items():
#     print(f'{k} = {v}')

# # filme2 = { 'nome': 'matrix',
# #          'ano': '1989',
# #          'diretor':'mamaco'
# # }


# # filme3 = {'nome':'sharek',
# #           'ano':'2007',
# #           'diretor':'Hugo'
# # }

# # locadora.append(filme)
# # locadora.append(filme2)
# # locadora.append(filme3)
# # for i, v in enumerate(locadora):
# #     print(f' {i+1}  {v}')

# values --> conferir o valor presente no indice/nome do dicionario
# keys --> conferir o indice dele (mostrado por nomes e não numeros)
# items --> mostrar tanto o indice quanto o valor referente a ele/ serve como enumerate
# del --> apaga algum valor do dicionario 
# copy --> faz uma copia de um dicionario e adiciona ele a uma lista

# estado = {}
# brasil = []
# for c in range(0, 2):
#     estado['uf'] = str(input('estado: '))
#     estado['sigla'] = str(input('sigla: '))
#     brasil.append(estado.copy())
# for e in brasil:
#     for t in e.values():
#         print(t)

aluno = {}

aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input(f'media de {aluno['nome']}: '))

print(f'o nome é {aluno["nome"]} ')
print(f'a media é {aluno["media"]} ')

if aluno['media'] >= 7:
    print('situação é aprovado(a)')
else:
     print('situação é reprovado(a)')

