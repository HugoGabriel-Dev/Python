ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota1: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opc = str(input('deseja continuar (s/n)? '))
    if opc in 'Nn':
        break
print('-='*30)
print(f'{'No':<3} {'NOME':<10} {'MEDIA':<3}')
print('-'*30)
for i, n in enumerate(ficha):
    print(f'{i:<3} {n[0]:<10} {n[2]:<3}')
print('-='*30)
while True:
    resp = int(input('qual aluno voce deseja ver as notas? (999 interrompe)'))
    if resp == 999:
        print('FINALIZANDO PROGRAMA!')
        break
    if resp <= len(ficha) - 1:
        print(f'as notas de {ficha[resp][0]} são {ficha[resp][1]}')
    