def voto (idade):

    ind = 2025 - idade
    if 18 <= ind <= 65:
        print(f'com {ind} anos: VOTO OBRIGATORIO! ')
    elif ind > 65:
        print(f'com {ind} anos: VOTO OPCIONAL! ')
    else:
        print(f'com {ind} anos: NÃO VOTA! ')


ano = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
voto(ano)    

    