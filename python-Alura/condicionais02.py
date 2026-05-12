atividade1 = int(input(f'Digite as horas da atividade --> '))
atividade2 = int(input(f'Digite as horas da atividade --> '))
atividade3 = int(input(f'Digite as horas da atividade --> '))
if atividade1 < 0 or atividade2 < 0 or atividade3 < 0:
    print("[ERROR], Número não pode ser negativo!!! ")
else:
    total_horas = atividade1 + atividade2 + atividade3
    print(f'O total de horas de todas as atividades é --> {total_horas}')